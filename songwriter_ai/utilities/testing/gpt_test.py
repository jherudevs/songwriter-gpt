import os
import sys
import io
from openai import OpenAI

# 🛠 Force stdout to UTF-8 (final boss fix)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Init
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("🛑 OPENAI_API_KEY not found.")
client = OpenAI(api_key=api_key)

# GPT call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant."},
        {"role": "user", "content": "I'm feeling a bit blah"}
    ],
    temperature=0.8,
    max_tokens=50
)

# Print result
print(f"🧪 Raw GPT response: {response.choices[0].message.content.strip()}")

