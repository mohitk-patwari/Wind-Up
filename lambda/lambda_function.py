"""
Wind-Up API — turns a phrase into a music box melody.

There is no language model here. The melody is composed from the phrase itself: the
text is hashed into a seed, scanned for mood, then developed the way a composer
develops a theme — state a short motif, then transpose it, invert it, stretch it,
reverse it, and land back on the tonic. The same phrase always returns the same
melody, which is the point: the phrase *is* the score.
"""

import hashlib
import json
import random

GRID = 0.25
LOW_MIDI, HIGH_MIDI = 60, 84           # C4 .. C6, the comb of the box

CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "content-type",
    "Access-Control-Allow-Methods": "POST,OPTIONS",
    "Content-Type": "application/json",
}

MODES = {
    "major":      [0, 2, 4, 5, 7, 9, 11],
    "minor":      [0, 2, 3, 5, 7, 8, 10],
    "pentatonic": [0, 2, 4, 7, 9],
}
NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

SLOW = {"quiet", "slow", "empty", "alone", "lonely", "rain", "night", "late", "tired",
        "grief", "sad", "still", "fog", "winter", "goodbye", "last", "half", "dusk",
        "waiting", "gone", "far", "soft", "sleep", "memory", "old", "grey", "gray"}
FAST = {"fast", "run", "bright", "loud", "party", "dance", "rush", "spark", "wild",
        "morning", "sun", "laugh", "chase", "electric", "hurry", "flash", "jump",
        "summer", "quick", "burst", "alive", "sharp", "neon"}

# Rhythmic cells, in beats.
CELLS = [[1.0], [0.5, 0.5], [0.75, 0.25], [0.5, 0.25, 0.25],
         [1.5], [0.25, 0.25, 0.5], [2.0], [0.5, 1.0]]

FIRST = ["Small", "Late", "Paper", "Quiet", "Half", "Blue", "Slow", "Last",
         "Winter", "Thin", "Bright", "Distant", "Folded", "Open", "Narrow"]
SECOND = ["Hours", "Window", "Signal", "Weather", "Room", "Station", "Light",
          "Machine", "Garden", "Circuit", "Tide", "Letter", "Engine", "Door"]


def _name(midi):
    return f"{NAMES[midi % 12]}{midi // 12 - 1}"


def _pitch(degree, scale, base=72):
    """A scale degree, possibly out of octave, mapped onto a tooth of the comb."""
    octave, idx = divmod(degree, len(scale))
    midi = base + 12 * octave + scale[idx]
    while midi > HIGH_MIDI:
        midi -= 12
    while midi < LOW_MIDI:
        midi += 12
    return midi


def compose(phrase, mode, rng):
    scale = MODES[mode]
    words = {w.strip(".,!?;:'\"").lower() for w in phrase.split()}

    tempo = 84 + 15 * len(words & FAST) - 12 * len(words & SLOW)
    tempo = max(54, min(132, tempo + rng.randint(-4, 4)))

    # 1. state a motif
    leap = 2 if len(phrase) < 30 else 3
    motif_len = rng.choice([3, 4, 4, 5])
    degrees = [rng.choice([0, 2, 4])]
    for _ in range(motif_len - 1):
        degrees.append(degrees[-1] + rng.choice([-2, -1, -1, 1, 1, 2, leap]))

    rhythm = []
    while len(rhythm) < motif_len:
        rhythm.extend(rng.choice(CELLS))
    motif = list(zip(degrees, rhythm[:motif_len]))

    # 2. develop it
    def transpose(m, by):
        return [(d + by, r) for d, r in m]

    def invert(m):
        pivot = m[0][0]
        return [(2 * pivot - d, r) for d, r in m]

    def augment(m):
        return [(d, min(r * 2, 2.0)) for d, r in m]

    def retrograde(m):
        return list(reversed(m))

    sections = [motif]
    for _ in range(3):
        prev = sections[-1]
        choice = rng.choice(["transpose", "transpose", "invert", "augment", "retrograde"])
        if choice == "transpose":
            sections.append(transpose(prev, rng.choice([-2, -1, 1, 2, 3])))
        elif choice == "invert":
            sections.append(invert(prev))
        elif choice == "augment":
            sections.append(augment(prev))
        else:
            sections.append(retrograde(prev))

    # 3. lay it out in time, with a breath between phrases
    notes, t = [], 0.0
    for section in sections:
        for degree, dur in section:
            if t >= 26:
                break
            dur = max(GRID, round(dur / GRID) * GRID)
            notes.append({"n": _name(_pitch(degree, scale)), "t": round(t, 2), "d": dur})
            t += dur
        t += rng.choice([0.0, 0.5, 0.5, 1.0])

    # 4. land on the tonic, held
    if t < 30:
        notes.append({"n": _name(_pitch(0, scale)), "t": round(t, 2), "d": 2.0})

    return tempo, notes[:64]


def _reply(status, body):
    return {"statusCode": status, "headers": CORS, "body": json.dumps(body)}


def lambda_handler(event, context):
    method = (event.get("requestContext", {})
                   .get("http", {})
                   .get("method", "POST")).upper()
    if method == "OPTIONS":
        return {"statusCode": 204, "headers": CORS, "body": ""}

    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _reply(400, {"error": "Send valid JSON."})

    phrase = str(body.get("phrase", "")).strip()[:200]
    mode = str(body.get("mode", "major")).lower()
    if mode not in MODES:
        mode = "major"
    if not phrase:
        return _reply(400, {"error": "Tell it a feeling first."})

    seed = int(hashlib.sha256(f"{phrase}|{mode}".encode()).hexdigest()[:16], 16)
    rng = random.Random(seed)

    try:
        tempo, notes = compose(phrase, mode, rng)
    except Exception as exc:                       # noqa: BLE001
        print(f"compose failure: {type(exc).__name__}: {exc}")
        return _reply(500, {"error": "The box jammed. Try winding it again."})

    if len(notes) < 4:
        return _reply(500, {"error": "That came out empty. Try another phrase."})

    return _reply(200, {
        "title": f"{rng.choice(FIRST)} {rng.choice(SECOND)}",
        "tempo": tempo,
        "mode": mode,
        "notes": notes,
        "lowMidi": LOW_MIDI,
        "highMidi": HIGH_MIDI,
    })