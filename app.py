from flask import Flask, request, jsonify, render_template
import pdfplumber
import os
import re
from groq import Groq

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text[:4000]

def simplify_paper(text):
    prompt = f"""You are a research paper simplifier. Read the following research paper and explain it in simple plain English.

Return ONLY this exact format. Do not use any asterisks, bullet points, dashes, or markdown. Plain text only:

ABOUT:
1-2 sentences about what the study is about.

WHAT THEY DID:
2-3 sentences explaining the methodology simply.

WHAT THEY FOUND:
2-3 sentences on key results.

WHY IT MATTERS:
1-2 sentences on real world impact.

TERMS:
Term1: explanation in one sentence.
Term2: explanation in one sentence.
Term3: explanation in one sentence.
Term4: explanation in one sentence.
Term5: explanation in one sentence.

Research paper:
{text}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    result = response.choices[0].message.content
    # Remove any stray asterisks
    result = re.sub(r'\*+', '', result)
    return result.strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simplify", methods=["POST"])
def simplify():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    if file.filename == "" or not file.filename.endswith(".pdf"):
        return jsonify({"error": "Please upload a valid PDF file"}), 400
    try:
        text = extract_text_from_pdf(file)
        if not text.strip():
            return jsonify({"error": "Could not extract text from PDF"}), 400
        result = simplify_paper(text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
