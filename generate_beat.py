import os
from songwriter_ai.utilities.prompting.deduction_engine import deduce_vibe_from_prompt
from songwriter_ai.utilities.prompting.naming_engine import name_my_stack
from songwriter_ai.utilities.audio.stacker import run_stacker
from songwriter_ai.utilities.prompting.prompt_engine import generate_lyric_line

if __name__ == "__main__":
    print("🧠 How are you feeling today?")
    mood = input("→ ")

    vibe = deduce_vibe_from_prompt(mood)
    print(f"🎧 Mood detected → Vibe: {vibe}")

    # Run the stacker (generates default filename)
    run_stacker(vibe_name=vibe)

    # Generate name using OpenAI
    stack_name = name_my_stack(mood, vibe)
    new_filename = f"{stack_name}.wav"

    # Rename latest stacked output
    stacks_dir = os.path.join("outputs", "stacks")
    files = sorted(os.listdir(stacks_dir), key=lambda f: os.path.getmtime(os.path.join(stacks_dir, f)), reverse=True)
    if files:
        latest_file = files[0]
        new_path = os.path.join(stacks_dir, new_filename)
        os.rename(os.path.join(stacks_dir, latest_file), new_path)
        print(f"📝 Renamed to: {new_filename}")

    # 🎤 Generate lyric line
    lyric = generate_lyric_line(vibe, mood)
    if lyric:
        print(f"\n📝 Lyric Idea: {lyric}")