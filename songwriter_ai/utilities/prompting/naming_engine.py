import os
from openai import OpenAI
from songwriter_ai.utilities.prompting.text_utils import normalize_text

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("🛑 OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)

def name_my_stack(user_mood: str, vibe: str) -> str:
    system_message = (
        "You're a beat-naming assistant. A user described how they're feeling, and a vibe was chosen for their beat.\n"
        "Your job is to name the final beat file. Give a short, poetic, or vibey title like you'd name a track.\n"
        "Respond with only 1-5 words. No punctuation or special characters. Underscore-separated words only.\n"
        "Example: 'neon rush' → 'neon_rush'"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Mood: {user_mood}\nVibe: {vibe}"}
            ],
            temperature=0.7,
            max_tokens=10
        )
        raw = response.choices[0].message.content.strip()
        cleaned = normalize_text(raw)
        return "_".join(cleaned.lower().split())[:50]
    except Exception as e:
        print(f"⚠️ Naming error: {e}")
        return f"{vibe}_beat"
