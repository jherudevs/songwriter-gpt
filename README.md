# 🎶 Songwriter GPT: Emotion-to-Beat Generator

An AI-powered music assistant that transforms your vibe and topic into a beat + lyric line.


## Loom Demo


## 🚀 Features
- Enter how you feel in the prompt
- AI analysis of input
- Loop created from input (drums + vibe)
- Starter lyrics deduced from input

## 🛠️ Tech Stack
- Python + Flask
- Librosa + Pydub
- OpenAI API
- HTML + audio output in-browser

## 📂 Project Structure
songwriter-gpt/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example         # Safe example file
├── loops/               # Sample loop folders (e.g. hype/, sad/, drums/)
├── outputs/             # Auto-generated (should be gitignored)
├── songwriter_ai/
│   └── utilities/
│       ├── audio/
│       ├── prompting/
│       ├── file_ops/
│       └── __init__.py
├── templates/
│   └── index.html
├── static/              # (optional CSS/JS)
└── venv/                # (ignored)


## 🔐 Setup
1. Clone this repo
2. Create `.env` with your OpenAI key
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run Locally
