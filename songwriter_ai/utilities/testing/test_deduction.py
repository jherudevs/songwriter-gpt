# test_deduction.py
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from songwriter_ai.utilities.prompting.deduction_engine import deduce_vibe_from_prompt

if __name__ == "__main__":
    print("🎤 How are you feeling today:")
    user_input = input("→ ")

    vibe = deduce_vibe_from_prompt(user_input)
    print(f"\n🎯 Deduced Vibe: {vibe}")

