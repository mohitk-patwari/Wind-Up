Limani Ndou

Limani Ndou

3m ago



I built an AWS Service Logo Game for the Weekend Creative Challenge. It is a fun quiz game with a timer, 3 lives, score tracking using AWS services.

Services used:

AWS Amplify: hosts the live frontend app and handles deployment from GitHub.

Amazon API Gateway: receives requests from the game and sends them to the backend.

AWS Lambda: runs the backend logic for saving scores and loading the leaderboard.

Amazon DynamoDB: stores player scores for the leaderboard.

Amazon CloudWatch: helps monitor logs and troubleshoot the backend.

Live game: 

https://main.d1wz3jwllt45af.amplifyapp.com/ 

Article: https://builder.aws.com/content/3HJocIt1JKmi9LTvaCpQVErtYyF/weekend-creative-challenge-aws-service-logo-game 

\#creative-expression #aws #awsamplify #awslambda #dynamodb #apigateway



0



0



Reply



Muhammad Usman

Muhammad Usman

Modified 14m ago



Student Builder Group Leader

Here is my submission for the Weekend Creative Challenge:

Roast Generator - a serverless AI app that writes short, funny PG-13 roasts in styles like Gen-Z, Shakespearean, or Corporate HR, with three heat levels.

Article: https://builder.aws.com/content/3HtlL53OLSyUO4oT32m2cZV0jWu/weekend-creative-challenge-roast-generator

Live app: http://ai-roast-generator.s3-website-us-east-1.amazonaws.com/ 

Repo: https://github.com/muhmdusman/aws-challenge-roast-generator 



0



0



Reply



Pamuda U. de A. Goonatilake

Pamuda U. de A. Goonatilake

18m ago



Student Builder Group Leader

My Submission: PlotTwist

Built an interactive branching storytelling app where every choice shapes what happens next, using React, TypeScript, a procedural story engine, and AWS Amplify Hosting.

Article Link: https://builder.aws.com/content/3HtiL1b85fa5xotbAnEliDfUvt1/weekend-creative-challenge-plottwist



0



0



Reply



Mohammed Mudasser

Mohammed Mudasser

19m ago



Really excited to share my project for the AWS Weekend Creative Challenge! 🚀

I built MoodCapsule — a creative AI application that transforms a daily text or voice journal entry into a multisensory memory capsule with an AI-generated mood, personalized poem, image, and spoken narration.

The project brings together Amazon Bedrock, Nova Lite, Nova Canvas, Amazon Transcribe, Amazon Polly, AWS Lambda, API Gateway, S3, and DynamoDB to turn a simple journal entry into something you can read, see, and hear.

It was a fun opportunity to combine my AI/ML experience with AWS cloud services and build something creative with a real end-to-end workflow.

Would love to hear your thoughts and feedback! 🙌

🔗 Full build \& architecture:

AWS Builder Center — MoodCapsule

\#AWS #AWSBuilder #AmazonBedrock #AmazonNova #GenerativeAI #AI #Serverless #CreativeAI #creative-expression



0



0



Reply



Felina Christy A

Felina Christy A

27m ago



Community Builder

Daybreak — a short, quiet thing to read in the morning.

You type how you're arriving today, however it comes — "big presentation and I keep second-guessing myself" — and get back one thing to read: a verse or a line, a short reflection written for what you actually said, a card you can keep, and a voice reading it to you.

Two things I didn't expect.

There was no text-to-image model available to me. Nova Canvas is Legacy, Titan Image is EOL, and Stability's Bedrock offering is editing-only. So I drew the card backgrounds procedurally in the browser instead — gradient, radial light, one motif per mood, grain, vignette, all seeded from the date. It turned out better than generation would have been: a calm app wants consistency rather than surprise, and when you control the pixels, contrast stops being a repair job and becomes something you can guarantee.

Scripture is never generated. All 31,095 verses of the World English Bible ship inside the app, and every verse shown is a byte-for-byte lookup. The model may name a reference; it never writes one. In Plain mode the encouraging line is written by the model — and applying the stricter rule there by mistake is how someone celebrating a new job got handed a line about not being lost. That story's in the article.

Built on Amazon Bedrock (Nova Lite), Amazon Polly (neural, SSML-paced), AWS Lambda, S3 and CloudFront.

📖 Article: https://builder.aws.com/content/3Htfek9g8N5B8FulFUjWiwvagx5/weekend-creative-challenge-daybreak

🔗 Live app: https://d3f7xjgvqvtpm2.cloudfront.net/ 

💻 GitHub: https://github.com/Felina14/daybreak 

Tell it how you're arriving. I'd like to know what it says to you.

\#creative-expression



0



0



Reply



abdullah haroon

abdullah haroon

28m ago



here's my submission:

VerseCraft AI transforms simple ideas and emotions into original poems using generative AI. Built with Groq and a serverless AWS architecture, the project explores how a focused creative experience can combine AI, web development, and AWS services.

app link: https://d3ahx0v89bhhzc.cloudfront.net/

article link: https://builder.aws.com/content/3HtkGCa82LXA3r1fLylgGwOr9kK/weekend-creative-challenge-versecraft-ai



1



0



Reply



Saumili Dutta

Saumili Dutta

32m ago



Hi,

my submission for this weekend challenge is SpillThrill.

It is a game of truth or dare built using S3, DynamoDB and Lambda.

Checkout my blog to learn more : https://builder.aws.com/content/3HtHPoRq6NaOijlikJUZDkgxb3U/weekend-creative-challenge-spillthrill

GitHub : https://github.com/aumiidutta/SpillThrill 

Feedbacks are welcome!



0



0



Reply



Shubhadip Chakrabarti

Shubhadip Chakrabarti

34m ago



My Submission: Ye Olde Stack Trace

Turned scary stack traces into 17th-century pirate ship logs and medieval bard ballads using Amazon Bedrock (Nova Micro), AWS Lambda, and AWS Amplify.

Article Link: https://builder.aws.com/content/3HMfAynYDbbLgqRG5itQ4sWOiqE/weekend-creative-challenge-ye-olde-stack-trace



0



0



Reply



Muhammad Bilal

Muhammad Bilal

44m ago



My AWS Weekend Creative Challenge entry is live!

I built “Pix-Riddle”, an AI-powered guessing game where every round starts with a fresh, poetic riddle generated by Amazon Bedrock (Nova). Instead of simply checking answers as right or wrong, the AI also understands close guesses and gives contextual feedback—so the game becomes a conversation between human creativity and machine imagination.

Built with Amazon Bedrock, Lambda, API Gateway, DynamoDB, and Amplify, with a global leaderboard to add a competitive twist.

Read the full article: https://builder.aws.com/content/3HthiVT1SzWmIkXwqe8AEsO52av/pix-riddle-ai-image-guessing-game



1



0



Reply



Kushneet Kaur

Kushneet Kaur

Modified 42m ago



Student Builder Group Leader

Weekend Creative Challenge: ASCII Architect 📐

Describe a system in plain English — "a CI pipeline that builds, tests and deploys a web app" — and get back an architecture diagram made entirely of text, ready to paste into a README, a commit message, or a terminal. No image hosting, no diagramming tool, and it shows up as a readable diff in git when someone changes it.

The interesting part: Nova Lite couldn't draw aligned boxes. Bottom edges kept coming out one character wider than tops, and three prompt rewrites didn't fix it. So I stopped asking it to draw — the model now returns the architecture as JSON and a renderer I wrote lays out the ASCII deterministically. Alignment became a property of the code instead of something to hope for from a model. The same trick fixed its habit of pointing databases into services.

Built with Amazon Bedrock (Nova Lite) + AWS Lambda + API Gateway + S3. One HTML file, no build step.

Article

Live app 

GitHub 



1



1



Reply



Kushneet Kaur

Kushneet Kaur

10m ago



Student Builder Group Leader

https://ascii-architect-015256609001-site.s3.us-east-1.amazonaws.com/index.html if the other link is not working 



Prakhar Shukla

Modified 52m ago



Weekend Creative Challenge: The Midnight Station 📻

A radio station that doesn't exist, broadcasting 2am–4am to almost nobody. Tune the dial to anything — "the swimming pool after closing" — and it comes on air and READS IT TO YOU. Four segments: a forecast for a place that isn't real, a dedication from an invented caller, an advert for a product that shouldn't exist, and a sign-off.

Amazon Bedrock (Nova Micro) writes the script, Amazon Polly speaks it in one of six neural voices. The VU meter is driven by a real Web Audio analyser, not an animation.

Turn your sound on for this one 🔊

🚀 Live: http://midnight-station-846719029074.s3-website-us-east-1.amazonaws.com/ 

💻 Source: https://github.com/Prakhar2025/midnight-station 

\#creative-expression #challenge



0



0



Reply



Vincent

Vincent

54m ago



here is my submission

https://builder.aws.com/content/3HtgtJgtgikVFxnB9kU4Eia8Lrv/weekend-creative-challenge-infrastructure-narrator



0



0



Reply



Akhyar

Akhyar

1h ago



Compliment Creature is a small AI-powered app that turns your day into a kind, funny message from a whimsical animal companion. Choose a creature, share how your day went, and receive an original compliment plus its quirky personality trait.

Aritcle: https://builder.aws.com/content/3Htfy7P4FqTv4dnuCJCzEjxJjUI/weekend-creative-challenge-compliment-creature

Github: https://github.com/real-akhyar/AWS-Weekend-Challenge-2/blob/main/article.md



1



2



Reply



Akhyar

Akhyar

now



Live APP: http://compliment-creature-892978057595-20260814.s3-website-us-east-1.amazonaws.com/



0



0



Reply



Muhammad Bilal

Muhammad Bilal

43m ago



Loved it!



0



0



Reply



Hide replies

Ritik Dhanotiya

Ritik Dhanotiya

1h ago



Student Builder Group Leader

🚀 Here is my submission for the AWS Weekend Creative Challenge — MoodPop ✨

I built MoodPop to turn everyday moods and situations into a tiny creative world with characters, stories, memes, and a mini-game. 🎭📖😂🎮

📝 Article:

https://builder.aws.com/content/3HtfySLO3o31VUof0TQCKu33uEi/weekend-creative-challenge-moodpop-turn-your-mood-into-a-tiny-world

🌐 Live Demo:

https://merry-tanuki-3cbd92.netlify.app/result 

💻 GitHub Repository:

https://github.com/Ritikdhanotiya07/MoodPop 

Would love to hear your feedback! ✨

\#MoodPop #WeekendCreativeChallenge



1



0



Reply



Iqra Urooj

Iqra Urooj

1h ago



Managing personal tasks efficiently had always been a personal challenge for me, which led me to develop the initial version of this todo application last year. When the AWS Weekend Creative Challenge was announced, I saw an ideal opportunity to completely revamp the project. My goal was to reimagine task management by incorporating fun, creative, and funky features—making the user experience interactive and dynamic so that completing daily work feels engaging rather than like a routine chore.

Core Architecture \& Key Features:

Fun \& Interactive Easter Eggs: Built-in playful elements including a Konami Code disco mode, logo confetti rockets, and responsive search animations to make task tracking enjoyable.

In-Browser Web Audio Engine: Implemented procedural sound synthesis (celebrations, actions, mode toggles) directly via the native Web Audio API, eliminating external asset dependencies.

Gamified Productivity Suite: Includes real-time streak tracking with custom cursor effects, task completion animations, a Pomodoro timer, and automatic localStorage persistence.

AWS Infrastructure: Deployed as a static web application on Amazon S3 utilizing static website hosting and custom bucket policies for global availability.

Full technical details, architecture diagrams, and implementation steps are documented in the article above.

Github repo:https://github.com/iqraurooj111/TASK-MASTER-PRO-

Article link:https://builder.aws.com/content/3HtZAd5WxtKpLf7A9S8mLI5fim6/weekend-creative-challenge-taskmaster-pro



0



0



Reply



Mohamed Ibrahim A

Mohamed Ibrahim A

1h ago



Just submitted my entry for the Weekend Creative Challenge! 🎲✨

Tiny Tale Toy: an AI-powered choose-your-own-adventure game where every branch, tension point, and choice is generated live by Amazon Bedrock. Pick your genre and protagonist, make tough decisions across a 5-chapter story, and receive a complete shareable narrative chronicle of your adventure!

Built with AWS Lambda (Python 3.12), Amazon API Gateway, Amazon Bedrock, and AWS Amplify.

📄 Article: https://builder.aws.com/content/3HtfN26MOUWBShfHvzElN5DgdWY/weekend-creative-challenge-tiny-tale-toy-an-ai-powered-choose-your-own-adventure-game

🚀 Live app: https://main.d3ouaihhnj43p9.amplifyapp.com/

💻 GitHub Repository: https://github.com/MdIbuA/tiny-tale-toy

Had a blast building this serverless storytelling engine. Would love to hear what wild adventures your playthroughs generate! 🧙‍♂️⚔️🚀



0



0



Reply



Shivam Gandhi

Shivam Gandhi

1h ago



Weekend Creative Challenge: Inkwell 🖋

A tiny serverless writing desk. Give it a theme — "a lighthouse that forgot the sea" — pick a form, and it writes you something small and strange. Four forms: a poem, a short story, three linked haiku, or five six-word stories. Every piece comes back with its own model-generated title, typed out onto a page torn from a notebook.

Built with Amazon Bedrock (Nova Micro) + Lambda + API Gateway + S3. No build step, one HTML file, one Python function.

📝 Article: https://builder.aws.com/content/3HtehLKASYsoby7zLunsA0XOoYq/weekend-creative-challenge-inkwell

🚀 Live app: http://inkwell-846719029074.s3-website-us-east-1.amazonaws.com/

💻 Source: https://github.com/SNG-8511/Inkwell

\#creative-expression #challenge



2



0



Reply



Ahmad Faraz

Ahmad Faraz

1h ago



Just submitted my entry for the AWS Weekend Creative Challenge!

I built Study Session Planner for Students — an AI-powered productivity app that creates personalized study plans, motivational messages, practice questions, and revision tips based on a student’s subject, available study time, and difficulty level.

Built with AWS PartyRock and Amazon Bedrock foundation models.

📝 Article:

https://builder.aws.com/content/3GQrjQUicxqc8kbvNbbSkL8hR5U/weekend-creative-challenge-study-session-planner-for-students

🚀 Live App:

https://partyrock.aws/u/ahmadafaraz/VjWJMjYET/Study-Session-Planner-for-Students 

Really enjoyed turning a simple student productivity idea into a working Generative AI application with AWS. Thanks for hosting the challenge! 🙌

\#creative-expression #challenge #GenerativeAI #PartyRock



1



0



Reply



Hafiz Syed Ashir Hassan

Hafiz Syed Ashir Hassan

1h ago



Community Builder

User Group Leader

Driftnote: Cast three words into the tide and receive a found letter, poem, rumor, or lullaby. Driftnote is a serverless creative toy, API Gateway, Lambda, and Amazon Bedrock Nova Lite turn ordinary words into messages washed ashore.

Article: https://builder.aws.com/content/3HsyzJFGYAb2kaxwAsUejaxYL4e/weekend-creative-challenge-driftnote



0



0



Reply



Thirumalaiboobathi B

Thirumalaiboobathi B

2h ago



Weekend Creative Challenge: Tinai Poet

Sangam Tamil poets had a rule: never name the emotion. Every situation belongs to one of five thinai — landscapes that carry the feeling by convention. Grief on a seashore at dusk is neithal.

Tinai Poet reads your situation into one of those five landscapes. Then runs backwards: Play mode hides the landscape and asks you to read it back out of the verse.

The five landscapes are hardcoded, not model-recalled — so it can't hallucinate a two-thousand-year-old tradition. Built on Bedrock, Amplify, and DynamoDB.

📝 https://builder.aws.com/content/3HtbcWImKXkqbWqsqavbcnaa2Rr/weekend-creative-challenge-tinai-poet



Joel Anarba Amuni

2h ago



Student Builder Group Leader

Built QuestForge, an AI-powered interactive text adventure where every choice shapes the story and the world remembers your decisions.

Article: https://builder.aws.com/content/3HtcPU7JqPMcOKmWNW2P4k1CfQH/weekend-creative-challenge-questforge



0



0



Reply



JITEESH GHODKE

JITEESH GHODKE

2h ago



🚀 Just shipped Plot Twist for the AWS Weekend Creative Challenge!

The idea was simple: give the app a story idea, choose how chaotic you want it to be, and let the story spiral from there. 📖🌀

But the fun starts after the first story — you can make it darker, funnier, more absurd, add a plot twist, or completely change the ending. One innocent sentence can turn into something completely ridiculous. 😂

This was also my first time taking a project from a basic HTML/CSS/JavaScript prototype to a publicly deployed AWS application. I got hands-on with AWS Lambda, Lambda Function URLs, CORS, HTTP requests, and AWS Amplify along the way. ☁️💻

🔗 Try Plot Twist:

https://staging.d3muc3nfeq87mp.amplifyapp.com/ 

📝 Full build story:

https://builder.aws.com/content/3HtdLhEaa1KevfBRxR0GXuNYdAn/weekend-creative-challenge-plot-twist

💻 Source:

https://github.com/jiteeshghodke456-del/awschallenge2026jiteeshghodke.git 

Give it a ridiculous idea and see how badly the story can go. 🌀😂

\#creative-expression #AWS #AWSLambda #AWSAmplify #Serverless #BuildInPublic 🚀



1



0



Reply



Cristhian Becerra

Cristhian Becerra

2h ago



Community Builder

User Group Leader

Built the AWS User Group Piura Giveaway Website for this challenge:

A serverless raffle platform that kills the most annoying moment at community events, picking "winners" who never showed up. Attendees scan a QR code to register on the spot, a real-time spinning wheel picks from only actual participants, and the admin panel manages multiple raffles simultaneously.

Built entirely with Kiro on Lambda + API Gateway + DynamoDB + S3 + CloudFront + Route 53, all Terraform-provisioned and AWS Free Tier friendly.

Article: https://builder.aws.com/content/3HQtNN6BCQqt9KfqYEhKg38edmD/weekend-creative-challenge-aws-user-group-piura-giveaway-website

Live app: https://awsugpiura.com/sorteo 

GitHub: https://github.com/cbecerrae/awsugpiura-giveaway-website 

\#creative-expression



1



0



Reply



Tanseer Khan

Tanseer Khan

2h ago



Community Builder

My Submission :

Weekend Creative Challenge: Verse Weaver

An AI poem loom built on Bedrock, Lambda, and a weekend's worth of curiosity.

https://builder.aws.com/content/3HtMmNIBEEP0TEEfLXuSdI2ebBS/weekend-creative-challenge-verse-weaver



1



0



Reply



Yuuki Yamashita

Yuuki Yamashita

2h ago



Community Builder

Just posted

Weekend Creative Challenge: Mood Poem Card

https://builder.aws.com/content/3Ht19yR1Jq2IbSeojYY8Pwr8kei/weekend-creative-challenge-mood-poem-card



0



0



Reply



Donald Raph

Donald Raph

2h ago



Student Builder Group Leader

Lets gooo

here is my challenge article https://builder.aws.com/content/3HLxUMPBzeAXxEoPy5FDLxhxW4N/weekend-creative-challenge-debugging-saga



0



0



Reply



Shinnosuke Yakumo

Shinnosuke Yakumo

2h ago



Community Builder

User Group Leader

Just submitted my entry for the Weekend Creative Challenge! 🎋Haiku Lens takes a photograph and gives back a haiku: three lines of Japanese in 5-7-5, an English rendering, and a kigo (the seasonal word every haiku needs). It then paints the poem onto a tanzaku card, with the Japanese running vertically down the right-hand side, and hands it back as a PNG you can keep.Built with Amazon Bedrock (Claude Sonnet 4.6), AWS Lambda, CloudFront + S3 and AWS CDK. The API is a Lambda Function URL hidden behind CloudFront with an Origin Access Control, so there is no public endpoint and no CORS preflight anywhere.The part I did not expect: language models cannot count mora, so a kana dictionary counts them in Python and sends anything that is not 5-7-5 back to the model with the exact numbers. When I let the model grade its own metre instead, it hit 5-7-5 every single time by inventing words that do not exist. 😅

📄Article:https://builder.aws.com/content/3HtXBi2v50mQ1XwrwOls27ePOd9/weekend-creative-challenge-haiku-lens

🚀 Live app: https://dxkfk8fx28w3s.cloudfront.net 

💻 GitHub: https://github.com/shinnosukeyakumo/haiku-lens There are four sample photos on the landing page if you do not have one handy. Thanks for a genuinely fun challenge!



0



0



Reply



Anshika Singh Sengar

Anshika Singh Sengar

Modified 2h ago



I turned my “too-pretty-to-throw-away” scraps into a little creative spark ✂️✨

Read my Builder Center article:

&#x20;https://builder.aws.com/content/3HtamNe7Arf4eY12kkbkbRuFySH/weekend-creative-challenge-whimsy-scraps

Try Whimsy Scraps: https://main.d7mb4xwhqxenp.amplifyapp.com 

Source code: https://github.com/theartydev/whimsy-scraps 



0



0



Reply



Shamnad Shaji

Shamnad Shaji

2h ago



Community Builder

I have also completed my Weekend Creative Challenge: Muse.

Muse is a tiny AI-powered muse for anyone staring at a blank page. You type a theme - anything from "a lighthouse keeper who talks to the sea" to "the last bus of the night" - pick either Story or Poem, and within seconds Amazon Bedrock's Nova Lite model writes a short, original piece built around that spark.

Article link: https://builder.aws.com/content/3HtbMxlvAvEHDwf8VLEZ70QkGJc/weekend-creative-challenge-muse

App Link: http://muse-story-generator-frontendbucket-lsjlljcgkumt.s3-website-us-east-1.amazonaws.com/



0



0



Reply



Gokul S

Gokul S

2h ago



Student Builder Group Leader

Excited to share my Weekend Creative Challenge submission: StorySpark — Turn a Moment Into a Mini Story! ✨

Turn an everyday moment into a creative mini-story with AI. Choose from Funny, Emotional, Adventure, or Fantasy, and StorySpark generates a unique story with a custom title and memorable quote. Built with Amazon Bedrock, AWS Strands Agents, Lambda, API Gateway, S3, CloudFront, and Terraform.

It was a fun experience building a creative AI app with AWS! 🚀 I'd love to hear what you think — feedback is always appreciated!

Article Link: https://builder.aws.com/content/3HtZAmk7rL5HXA1cvbcpsgVAQ46/weekend-creative-challenge-storyspark-turn-a-moment-into-a-mini-story

Demo app : https://d1yah88u6k8wno.cloudfront.net/ 



0



0



Reply





Siva Abishikth Mylavarapu

Modified 2h ago



Excited to share my Weekend Creative Challenge submission: Infinite Mashup Studio! Combine unexpected ideas, fuse them with AI, and discover original creations complete with artwork, stories, narration, and more. It was a fun project to build with Amazon Bedrock and AWS serverless services. I'd love to hear what you guys think feedback is always appreciated!

Article Link: https://builder.aws.com/content/3Hk3A4A62DsjLmxz7szZGctQX55/weekend-creative-challenge-infinite-mashup-studio

App Link: https://infinite-mashup-studio.netlify.app 



0



0



Reply



Roomify

Roomify

2h ago



My Creative Cloud Toy: The Cloud Architect Excuse Generator

When I saw the prompt for this AWS Weekend Challenge to build a "Creative App," my mind immediately went to the shared struggles of every developer and cloud engineer. We all know the sinking feeling of a failed deployment, a sudden latency spike, or a mysterious database crash at 2 AM. Instead of stressing about it, I wanted to build a tool that lets us laugh at the chaos.

That was the inspiration behind the Cloud Architect Excuse Generator—a generative AI app that creates hilarious, highly technical (and completely ridiculous) excuses for why your infrastructure is currently broken.

What I Built

The Cloud Architect Excuse Generator is an interactive, AI-powered web toy. The premise is simple: the user inputs the current disaster they are facing. For example, they might type "the production database was accidentally dropped," or "the Kubernetes cluster is stuck in a crash loop."

Once the user hits submit, the application leverages generative AI to craft a plausible-sounding but entirely nonsensical technical excuse. For instance, it might generate: "Due to unexpected solar flare interference interacting with our multi-region BGP routing tables, the microservices temporarily achieved sentience and decided to drop the database to optimize their own latency."

It's a fun, lightweight way to express the creative side of software engineering, turning our daily frustrations into a moment of humor.

The AWS Architecture

To build this application rapidly without getting bogged down in infrastructure provisioning, I turned to PartyRock, an Amazon Bedrock Playground.

PartyRock provided the absolute perfect environment for this challenge. Instead of manually provisioning EC2 instances, setting up API Gateways, writing Lambda functions, and configuring IAM roles to interact with generative AI APIs, I was able to focus entirely on the creative aspect of the application.

Under the hood, the application is completely powered by Amazon Bedrock. It utilizes advanced foundation models to process the user's input, combine it with a hidden prompt constraint (instructing the AI to use excessive buzzwords and complex cloud terminology), and generate the final output. Because PartyRock runs natively on AWS, it handles all the scaling, hosting, and API interactions seamlessly.

What I Learned

This project was a fantastic exercise in rapid prototyping with Generative AI. In a traditional software development lifecycle, building a natural language processing app would take days or weeks of configuring endpoints and managing credentials.

By using PartyRock and Amazon Bedrock, I learned just how fast the iteration cycle can be. I spent most of my time refining the "system prompt" to ensure the AI's tone was perfectly balanced between technically accurate terminology and absolute absurdity. I learned that prompt engineering is less about coding and more about directing an actor—giving the model the right context, constraints, and personality to produce the desired creative output.

Furthermore, building this reinforced how democratized AI has become through services like Amazon Bedrock. The ability to go from an idea to a globally accessible, AI-powered web application in a single afternoon is a testament to the power of modern cloud services.

I hope you enjoy playing with the Cloud Architect Excuse Generator. Next time your pipeline fails, you'll know exactly what to tell your manager!

App Link: https://partyrock.aws/u/roomify1234/GUGDML3kf/Cloud-Architect-Blame-Excuse-Generator 



0



1



Reply



Saumili Dutta

Saumili Dutta

37m ago



FYI,

you have to write this in a blog along with the mentioned title and tag to qualify for the challenge and not as a comment. Then copy paste your blog link here in the comments section. And let this comment be, add a new comment...

Rooting for u to win



0



0



Reply



Hide replies

Stephen Fisher

Stephen Fisher

2h ago



I don't understand none of this stuff.



0



0



Reply



Gabriel

Gabriel

3h ago



Just submitted my entry for the Weekend Creative Challenge! 🎭

Excuse Generator: an AI-powered app that generates the perfect excuse for any situation, with an absurdity level you control (from plausible to completely insane) and a "Make It Worse" button for when it's not ridiculous enough yet.

Built with AWS Lambda, Amazon Bedrock (Nova Lite), and Amplify.

📄 Article: https://builder.aws.com/content/3HtToFfgVfAwTfmejM6ELuY2YKo/weekend-creative-challenge-excuse-generator

🚀 Live app: https://staging.d2usi4yqrsmlvh.amplifyapp.com/ 

💻 GitHub Repository: https://github.com/gabri3lV/Excuse-Generator-AI 

Had a lot of fun (and a few CORS headaches) putting this together this weekend. Would love to hear your excuses if the app gives you one worth sharing! 😄



1



0



Reply



S Srinuvas Rao

S Srinuvas Rao

3h ago



Just deployed my entry for the Weekend Creative Challenge! Check out the "Daily Vibe Check"—a completely serverless app powered by AWS Amplify, Lambda, and the brand-new Amazon Bedrock Nova models to turn your mood into original AI art and custom quotes. #creative-expression

https://builder.aws.com/content/3HtP35wOdGeQbvraEUkxeUJqUI6/weekend-creative-challenge-daily-vibe-check-mood-board-maker



0



0



Reply



Mrugesh Kulkarni

Mrugesh Kulkarni

Modified 3h ago



Excited to share my submission for the project challenge.

With this challenge I pushed myself to learn new things like AWS Amplify and learn more things about AWS Lamda, Bedrock, IAM and Hosting using S3.

Published Article : https://builder.aws.com/content/3HtPX52Xq8YFaHuEGh9OObGzZsl/weekend-creative-challenge-inkling

Deployed Project Link : https://main.d2skrf9bjoodwf.amplifyapp.com/ 

Thankyou for a great challenge.



1



0



Reply



Amitabh Soni 

Amitabh Soni

3h ago



Community Builder

Excited to submit my project for the challenge! 🚀

BackBench AI transforms nostalgic school memories into 4 creative artifacts (diary, teacher remarks, school magazine, and Bollywood script) using Amazon Bedrock Nova Lite and AWS Amplify.

Published Article

Live App 

Thanks for putting together a great challenge!



1



0



Reply



Saumili Dutta

Saumili Dutta

4h ago



Hi,

my submission for this weekend challenge is SpillThrill.

It is a game of truth or dare built using S3, DynamoDB and Lambda.

Blog link

GitHub repo 

Feedbacks are welcome!



0



0



Reply



Fahad Khalid

Fahad Khalid

4h ago



Student Builder Group Leader

My Weekend Creative Challenge submission is live! ✨

I built Wonderloom, a mood-based micro-story generator, and deployed it on AWS using Amazon S3 static website hosting.

Article:

https://builder.aws.com/content/3HtNo3kmDDt9dekJGbdR4wy4bh6/weekend-creative-challenge-wonderloom

Try it here: http://wonderloom-888635225506-20260814.s3-website-ap-southeast-2.amazonaws.com 

GitHub:

https://github.com/fahadkhalid695/Builder-center-Weekly-challenge.git 

\#creative-expression



0



0



Reply



Tanseer Khan

Tanseer Khan

4h ago



Community Builder

My Submission :

Weekend Creative Challenge: Verse Weaver

An AI poem loom built on Bedrock, Lambda, and a weekend's worth of curiosity.

https://builder.aws.com/content/3HtKjxC3hQETZmlDd2IZHdJqgM4/weekend-creative-challenge-verse-weaver



0



0



Reply

Shikaram Ruthika

4h ago



Student Builder Group Leader

Hey Ben! Just completed the Weekend Creative Challenge 🎉

Built Roast My Bio — an AI app that roasts your LinkedIn or Twitter bio in 3 funny sentences using Amazon Bedrock Nova Lite.

🔥 Live app: http://roast-my-bio-app-863852.s3-website-us-east-1.amazonaws.com 

📝 Article: https://builder.aws.com/content/3HtHa7RuikJRz53cKv6Fe5Ro5b9/weekend-creative-challenge-roast-my-bio

🐙 GitHub: https://github.com/Hackcode18/roast-my-bio 

Stack: S3 + Lambda + API Gateway + Bedrock Nova Lite — all on Free Tier. Built and deployed in one morning. Super fun challenge, learned a lot about Bedrock's API format the hard way 😅



1



0



Reply



Prasad Dalvi

Prasad Dalvi

5h ago



Just submitted my entry for the AWS Weekend Creative Challenge 🎮

Built “Once Upon an AI Adventure” — a tiny text adventure game where nothing is pre-written. Amazon Bedrock (Claude Haiku 4.5) generates every scene and choice in real time, making every playthrough unique.

In my adventure, I faced a spectral guardian who challenged me with a riddle 🐉

Read the full article: https://builder.aws.com/content/3HfYnogUu621kL0yvEdgIFYNKEp/weekend-creative-challenge-once-upon-an-ai-adventure

\#CreativeExpression #AWS #GenAI



2



0



Reply



Sameer Joshi

Sameer Joshi

5h ago



Great



0



0



Reply



Amudha Balamurugan

Amudha Balamurugan

5h ago



Community Builder

Love this challenge!



0



0



Reply



Someshh Rout

Someshh Rout

5h ago



Woww

Translate





0



0



Reply



Aryan Vijaykar

Aryan Vijaykar

Modified 5h ago



Student Builder Group Leader

Check this out:

https://builder.aws.com/content/3Ht8Tztbhnrn5u6BL8pu2ywDXeJ/weekend-creative-challenge-meme-remix-booth



0



0



Reply



Naman tyagi 18

Naman tyagi 18

5h ago



nice



0



0



Reply



Yoga

Yoga

6h ago



Hi, I wanted to send my article here: https://builder.aws.com/content/3Ht5ZWnzNolnohOxEUslWNSi810/weekend-creative-challenge-pujangga-poem-generator.

I created Pujangga, an AI Indonesian poem/verse generator. It writes pantun, gombal (pick-up lines), rap bars, captions, and puisi from any theme, and can even reply to your pantun. Built serverless with Amazon Bedrock (Nova), Lambda, API Gateway, and DynamoDB. Would love feedback!

\#creative-expression



0



0



Reply



Sri Monishan Robertkumar

Sri Monishan Robertkumar

6h ago



Student Builder Group Leader

I built and published MoodMeme Studio for the AWS Builder Center Weekend Creative Challenge.

MoodMeme Studio is a creative app deployed with AWS Amplify Hosting. It turns moods and ideas into meme captions, micro-stories, image prompts, and downloadable poster cards.

Builder Center article:

https://builder.aws.com/content/3Ht6PSMW8FnHwikAKniD2oV4K6r/weekend-creative-challenge-moodmeme-studio

Live app:

https://production.d13py1v0pps9bd.amplifyapp.com/ 

\#creative-expression



0



0



Reply



Sunil Goswami

Sunil Goswami

6h ago



This is a fantastic challenge! Excited to build something creative, put AWS skills into practice, and see what everyone comes up with. Looking forward to the weekend!





Thakor Tanmay

7h ago



Nice work 👍🏿 👍🏿 👍🏿



0



0



Reply



Christian Perez

Christian Perez

8h ago



Community Builder

User Group Leader

This is wonderfully creative. I love this weekend challenge!



0



0



Reply





