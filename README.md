# Wind-Up — run and deploy

Describe a feeling → Amazon Bedrock (Nova Micro) composes a melody → Python quantizes
it → a punched paper strip scrolls through a music box and plays it.

```
windup/
├── lambda/lambda_function.py   the prompt + the quantizer
├── frontend/index.html         the whole UI, one file
├── deploy.sh                   creates everything on AWS
├── ARTICLE.md                  Builder Center draft (877 words)
└── README.md
```

## Before you run anything

**AWS CLI configured** — `aws sts get-caller-identity` must return your account.
If not: `aws configure` with an access key from IAM.

That's it. You do **not** need to enable Bedrock model access — that console page was
retired. Serverless foundation models now switch on automatically the first time your
account invokes them, in every commercial region. Nova Micro is an Amazon model, so
there's no use-case questionnaire (that applies to Anthropic models) and no AWS
Marketplace step. `deploy.sh` grants the Lambda `bedrock:InvokeModel`, and the first
melody you generate is what activates the model.

## Deploy

```bash
cd windup
bash deploy.sh
```

It prints a live URL at the end. Roughly two minutes.

To redeploy after any edit, run the same command again — it's idempotent.

## Test it before you submit

- Open the URL in an **incognito window** (this catches public-access mistakes).
- Try all three modes.
- Try it on your phone.
- Open DevTools → Network → confirm the POST returns 200.

If you get **502 "The box jammed"**:
```bash
aws logs tail /aws/lambda/windup-api --since 5m --region us-east-1
```
`AccessDeniedException` here means IAM, not model access — check that the
`bedrock-invoke` inline policy landed on the role, and that you're invoking in the same
region the role was set up for. A brand-new account occasionally needs 30–60 seconds
after the very first invoke before the model is fully live; try winding it a second time.

## Run locally (optional)

```bash
cd frontend && python3 -m http.server 8000
```
Set `API_URL` at the top of `index.html` to your Function URL first.

## Cost

Free Tier. Nova Micro is fractions of a cent per melody; Lambda and S3 at this volume
round to zero. To tear it all down:

```bash
aws lambda delete-function --function-name windup-api --region us-east-1
aws s3 rb s3://windup-<ACCOUNT_ID>-site --force
aws iam delete-role-policy --role-name windup-lambda-role --policy-name bedrock-invoke
aws iam detach-role-policy --role-name windup-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam delete-role --role-name windup-lambda-role
```
