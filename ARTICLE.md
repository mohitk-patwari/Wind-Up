# Weekend Creative Challenge: Wind-Up

> Tag on Builder Center: **#creative-expression**
> Replace every ⟨…⟩ placeholder before publishing.

---

Every entry I read in this challenge made something you look at — a poem, a story, a
meme, a diagram. I wanted to make something you *hear*. So I built Wind-Up: you
describe a feeling, and a music box punches a paper strip and plays it back to you.

**Live app:** ⟨your S3 website URL⟩
**Source:** ⟨your GitHub repo URL⟩

## Vision and what the app does

Type something like *"the last train home, half empty"*, pick major, minor or
pentatonic, and turn the crank. A strip of punched paper scrolls through the window of
the box, left to right, and each hole sounds a note as it passes the comb. You can save
the strip as an SVG and keep it.

The same phrase always produces the same melody. That is deliberate. Your sentence
isn't a prompt that gets interpreted — it *is* the score. Change one word and you get a
different piece; type it again tomorrow and you get your piece back.

The metaphor does real work rather than sitting on top as decoration. A music box has
hard physical limits: a fixed comb of about two octaves, one note at a time, holes that
either exist at a position or don't. Those constraints shaped every decision in the
composer.

## How I built it

My original plan was to have Amazon Bedrock write the melody as JSON. I built the whole
pipeline that way — prompt, parser, a quantizer to snap the model's output onto a beat
grid and into the right key, because language models cannot count beats and the rhythms
came back as drift like 1.37 and 0.83.

Then Bedrock returned `ValidationException: Operation not allowed` on every model and
every operation in my account — Converse and InvokeModel alike, Nova Micro through Nova
Premier. Not an IAM problem: it failed identically when I called it directly from the
CLI as myself, so it was above my account entirely.

I had a working frontend, a working API, and a dead brain. With hours left, I had a
choice: abandon the project or write the composer myself.

Writing it myself turned out to be the better project. Here is what the Lambda does now:

1. **Seed.** The phrase is hashed to a 64-bit integer that seeds a `random.Random`.
   Determinism comes free — same phrase, same melody, forever.
2. **Mood.** The words are checked against two small vocabularies. Words like *empty,
   late, rain, half* pull the tempo down; *bright, run, morning, spark* push it up.
   "The last train home, half empty" lands at 54 bpm. "Bright summer morning, running"
   lands at 128.
3. **Motif.** A three-to-five note figure is generated as scale degrees, with steps
   weighted toward seconds and the occasional leap. Its rhythm is assembled from a
   bank of eight rhythmic cells.
4. **Development.** This is the part that makes it sound composed rather than random.
   The motif is put through four transformations drawn from actual compositional
   practice — transposition, inversion around its first note, augmentation (every
   duration doubled), and retrograde. Each section transforms the one before it, so
   the piece stays recognisably about one idea while never repeating exactly.
5. **Cadence.** A breath of rest between sections, then it lands on the tonic, held for
   two beats.

Working in scale degrees rather than pitches means every note is in key by
construction — there is no wrong note to filter out, because a wrong note cannot be
represented. Degrees that fall off the end of the comb get folded back an octave.

Playback is Tone.js in the browser: a `PolySynth` of FM voices with a near-instant
attack and no sustain, which is close to how a plucked metal tooth actually behaves,
through a small reverb. The scrolling strip is an SVG translated on each animation frame
against `Tone.Transport.seconds`, so the paper and the audio read from the same clock and
cannot drift apart.

Two smaller things that cost me time. Browsers will not start audio without a user
gesture, so `await Tone.start()` has to run inside the click handler, before the fetch.
And Lambda Function URLs returned `403 Forbidden` no matter how correct my resource
policy was — `AuthType: NONE`, `Principal: "*"`, condition matching — so I put an HTTP
API in front instead and it worked first try. If you hit that wall, stop debugging the
policy and switch.

## AWS services and architecture

```
Browser (Amazon S3 static website)
   │  POST { phrase, mode }
   ▼
Amazon API Gateway (HTTP API)
   │
   ▼
AWS Lambda (Python 3.12) — the composer
```

- **AWS Lambda (Python 3.12)** runs the composer. No dependencies beyond the standard
  library; the deployment package is under 3 KB and it responds in about 2 ms.
- **Amazon API Gateway (HTTP API)** is the public endpoint, with CORS configured on the
  API rather than in application code.
- **Amazon S3** serves the frontend as a static website. One HTML file, no build step.
- **Amazon CloudWatch Logs** is how I diagnosed every failure above, including the
  Bedrock one.
- **AWS IAM** for the execution role.

All Free Tier.

## What I learned

The real lesson was about dependency. I had treated a hosted model as infrastructure —
assumed-present, like a database. When it vanished I discovered the interesting part of
my project had been outsourced. Rewriting the composer by hand took about ninety
minutes and taught me more about music than the prompt ever would have: I had to learn
what inversion and augmentation actually are to implement them.

I also learned that constraints are generative. Working in scale degrees rather than
absolute pitches eliminated a whole class of bug. Building for a comb of 25 teeth made
the range problem trivial. The music box wasn't just a theme — it was the spec.

And practically: when a managed service fails identically from the CLI and from Lambda,
stop debugging your own code. That one observation saved me an hour.

Wind it up and tell it something. I'd like to know what it plays for you.

**#creative-expression**