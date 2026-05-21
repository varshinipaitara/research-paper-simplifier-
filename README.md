# 📄 Research Paper Simplifier

Upload any research paper (PDF) and get a plain English breakdown instantly.

## What it does
- Extracts text from uploaded PDF
- Uses Claude AI to simplify the paper into 5 clear sections:
  - What the study is about
  - What they did (methodology)
  - What they found (results)
  - Why it matters
  - Difficult terms explained

## Tech Stack
- **Backend:** Python + Flask
- **AI:** Anthropic Claude API
- **PDF Parsing:** pdfplumber
- **Frontend:** HTML + CSS + Vanilla JS

## Setup

1. Clone the repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your API key:
   ```
   export ANTHROPIC_API_KEY=your_key_here
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open `http://localhost:5000`

## Deploy (Render)
- Connect your GitHub repo on render.com
- Set `ANTHROPIC_API_KEY` as an environment variable
- Set start command: `python app.py`
- Done — free hosting!

## Screenshots
(Add screenshots here after running)
