# songwriter_ai/utilities/prompting/prompt_engine.py

import os
from openai import OpenAI
from songwriter_ai.utilities.prompting.text_utils import normalize_text

# Safely load API key from env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("🛑 OPENAI_API_KEY not found in environment variables.")

# Initialize client
client = OpenAI(api_key=api_key)

def generate_lyric_line(vibe, topic):
    """Generate a single lyric line using OpenAI v1 client."""
    prompt = f"Write a single line of lyrics in a {vibe} vibe about {topic}. Make it poetic but natural."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a talented songwriter assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=60,
        )
        raw = response.choices[0].message.content.strip()
        return normalize_text(raw)

    except Exception as e:
        print(f"⚠️ Error generating lyrics: {e}")
        return None
