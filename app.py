from flask import Flask, request, render_template, send_from_directory
from pathlib import Path
import os

# --- Backend pipeline imports ---
from songwriter_ai.utilities.prompting.deduction_engine import deduce_vibe_from_prompt
from songwriter_ai.utilities.audio.stacker import run_stacker
from songwriter_ai.utilities.prompting.naming_engine import name_my_stack
from songwriter_ai.utilities.prompting.prompt_engine import generate_lyric_line

# --- Pulls API key ---
from dotenv import load_dotenv

app = Flask(__name__)
STACKS_DIR = Path("outputs/stacks")

@app.route("/", methods=["GET", "POST"])
def index():
    output_file = None
    lyric = None

    if request.method == "POST":
        user_prompt = request.form["feeling"]

        # Step 1: Deduce vibe
        vibe = deduce_vibe_from_prompt(user_prompt)

        # Step 2: Generate beat stack
        run_stacker(vibe_name=vibe)

        # Step 3: Rename most recent stack
        stack_name = name_my_stack(user_prompt, vibe)
        new_filename = f"{stack_name}.wav"

        files = sorted(STACKS_DIR.glob("*.wav"), key=os.path.getmtime, reverse=True)
        if files:
            latest = files[0]
            renamed_path = STACKS_DIR / new_filename
            latest.rename(renamed_path)
            output_file = new_filename

        # Step 4: Generate lyric
        lyric = generate_lyric_line(vibe, user_prompt)

    return render_template("index.html", output_file=output_file, lyric=lyric)

@app.route("/outputs/stacks/<filename>")
def serve_output(filename):
    return send_from_directory(STACKS_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
