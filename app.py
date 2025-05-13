# app.py

from flask import Flask, render_template, request
import random
from pathlib import Path
from songwriter_ai.utilities.audio.align import auto_align_vibe_to_drums
from songwriter_ai.utilities.prompting.prompt_engine import generate_lyric_line

app = Flask(__name__)

VIBE_DIR = Path("loops")
DRUM_DIR = VIBE_DIR / "drums"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def get_loop(vibe):
    vibe_path = VIBE_DIR / vibe
    loops = list(vibe_path.glob("*.wav"))
    return random.choice(loops) if loops else None

def get_drum():
    loops = list(DRUM_DIR.glob("*.wav"))
    return random.choice(loops) if loops else None

@app.route("/", methods=["GET", "POST"])
def index():
    generated_lyric = None
    output_file = None

    if request.method == "POST":
        vibe = request.form["vibe"]
        topic = request.form["topic"]

        vibe_loop = get_loop(vibe)
        drum_loop = get_drum()

        if not vibe_loop or not drum_loop:
            return render_template("index.html", error="Missing loops.")

        output_path = OUTPUT_DIR / f"{vibe}_{topic.replace(' ', '_')}_stack.wav"
        auto_align_vibe_to_drums(str(vibe_loop), str(drum_loop), str(output_path))
        generated_lyric = generate_lyric_line(vibe, topic)
        output_file = f"/outputs/{output_path.name}"

    vibes = [d.name for d in VIBE_DIR.iterdir() if d.is_dir() and d.name != "drums"]
    return render_template("index.html", vibes=vibes, lyric=generated_lyric, audio_path=output_file)

if __name__ == "__main__":
    app.run(debug=True)
