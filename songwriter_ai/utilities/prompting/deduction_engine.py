import os
import random
from openai import OpenAI
from songwriter_ai.utilities.prompting.text_utils import normalize_text
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("🛑 OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)

def deduce_vibe_from_prompt(user_prompt: str) -> str:
    system_message = (
        "You're a music assistant. A user tells you how they feel today.\n"
        "Your job is to translate that emotional state into one vibe for a beat.\n"
        "Even if the input is vague, sarcastic, or unclear (e.g. 'ehh', 'i'm fine', 'idk'), do your best to infer the closest mood.\n"
        "Respond with only one of these vibe tags: hype, sad, romantic, angry.\n"
        "If you're unsure, pick the most likely based on tone. Reply with just the vibe word. No punctuation."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            max_tokens=5
        )
        raw = response.choices[0].message.content.strip()
        vibe = normalize_text(raw).lower()
        return vibe
    except Exception as e:
        print(f"⚠️ Deduction error: {e}")
        fallback = random.choice(["hype", "sad", "romantic", "angry"])
        print(f"🎲 Fallback vibe used: {fallback}")
        return fallback
