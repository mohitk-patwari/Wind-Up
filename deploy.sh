#!/usr/bin/env bash
# Wind-Up — deploy everything. Run from the windup/ folder:  bash deploy.sh
set -euo pipefail

REGION="${REGION:-us-east-1}"
FN=windup-api
ROLE=windup-lambda-role

ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
BUCKET="windup-${ACCOUNT}-site"
echo "→ account ${ACCOUNT} · region ${REGION} · bucket ${BUCKET}"

# ---------------------------------------------------------------- 1. IAM role
if ! aws iam get-role --role-name "$ROLE" >/dev/null 2>&1; then
  echo "→ creating IAM role"
  aws iam create-role --role-name "$ROLE" --assume-role-policy-document '{
    "Version":"2012-10-17",
    "Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}' >/dev/null
  aws iam attach-role-policy --role-name "$ROLE" \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
  aws iam put-role-policy --role-name "$ROLE" --policy-name bedrock-invoke \
    --policy-document '{
      "Version":"2012-10-17",
      "Statement":[{"Effect":"Allow","Action":["bedrock:InvokeModel"],"Resource":"*"}]}'
  echo "  waiting 12s for the role to propagate…"; sleep 12
fi
ROLE_ARN=$(aws iam get-role --role-name "$ROLE" --query Role.Arn --output text)

# ---------------------------------------------------------------- 2. Lambda
echo "→ packaging lambda"
( cd lambda && rm -f ../function.zip && zip -qr ../function.zip lambda_function.py )

if aws lambda get-function --function-name "$FN" --region "$REGION" >/dev/null 2>&1; then
  aws lambda update-function-code --function-name "$FN" --region "$REGION" \
    --zip-file fileb://function.zip >/dev/null
  aws lambda wait function-updated --function-name "$FN" --region "$REGION"
else
  aws lambda create-function --function-name "$FN" --region "$REGION" \
    --runtime python3.12 --handler lambda_function.lambda_handler \
    --role "$ROLE_ARN" --zip-file fileb://function.zip \
    --timeout 30 --memory-size 512 >/dev/null
  aws lambda wait function-active-v2 --function-name "$FN" --region "$REGION"
fi

# ---------------------------------------------------------------- 3. Function URL
aws lambda create-function-url-config --function-name "$FN" --region "$REGION" \
  --auth-type NONE --cors '{"AllowOrigins":["*"],"AllowMethods":["POST"],"AllowHeaders":["content-type"]}' \
  >/dev/null 2>&1 || true
aws lambda add-permission --function-name "$FN" --region "$REGION" \
  --statement-id public-url --action lambda:InvokeFunctionUrl \
  --principal "*" --function-url-auth-type NONE >/dev/null 2>&1 || true

API_URL=$(aws lambda get-function-url-config --function-name "$FN" --region "$REGION" \
  --query FunctionUrl --output text)
API_URL="${API_URL%/}"
echo "→ api: $API_URL"

# ---------------------------------------------------------------- 4. S3 site
aws s3api create-bucket --bucket "$BUCKET" --region "$REGION" \
  $( [ "$REGION" = "us-east-1" ] || echo "--create-bucket-configuration LocationConstraint=$REGION" ) \
  >/dev/null 2>&1 || true
aws s3api put-public-access-block --bucket "$BUCKET" \
  --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-bucket-policy --bucket "$BUCKET" --policy "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{\"Sid\":\"PublicRead\",\"Effect\":\"Allow\",\"Principal\":\"*\",
    \"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::${BUCKET}/*\"}]}"
aws s3 website "s3://${BUCKET}" --index-document index.html

echo "→ injecting api url and uploading"
mkdir -p build
sed "s|REPLACE_WITH_YOUR_LAMBDA_FUNCTION_URL|${API_URL}|" frontend/index.html > build/index.html
aws s3 cp build/index.html "s3://${BUCKET}/index.html" \
  --content-type "text/html" --cache-control "no-cache" >/dev/null

echo
echo "──────────────────────────────────────────────"
echo " LIVE:  http://${BUCKET}.s3-website-${REGION}.amazonaws.com"
echo "──────────────────────────────────────────────"
