# 📄 Research Paper Simplifier

An AI-powered web app that simplifies any research paper into plain English. Upload a PDF and instantly get a jargon-free breakdown.

## What it does
Upload any research paper PDF and get a simple breakdown in 5 sections:
- **About** — What the study is about
- **What They Did** — Methodology in simple terms
- **What They Found** — Key results
- **Why It Matters** — Real world impact
- **Terms Simplified** — Difficult words explained

## Tech Stack
| Part | Tech |
|---|---|
| Backend | Python + Flask |
| AI | Groq API (LLaMA 3.3 70B) |
| PDF Parsing | pdfplumber |
| Frontend | HTML + CSS + JavaScript |
| Deployed on | Render |

## Setup Locally

1. Clone the repo:
   ```
   git clone https://github.com/varshinipaitara/research-paper-simplifier-.git
   cd research-paper-simplifier-
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Get a free Groq API key at [console.groq.com](https://console.groq.com)

4. Set the API key:
   ```
   set GROQ_API_KEY=your_key_here
   ```

5. Run the app:
   ```
   python app.py
   ```

6. Open `http://localhost:5000`

## Live Demo
Check out the live app on Render!
