from flask import Blueprint, render_template, request, jsonify
from groq import Groq
import os

main = Blueprint("main", __name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/voice", methods=["POST"])
def voice():
    data = request.get_json()
    user_text = data.get("text", "")

    if not user_text:
        return jsonify({"response": "I didn’t catch that."})

    try:
        chat_completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # ✅ stable and fast
    messages=[{"role": "user", "content": user_text}],
    )
        ai_response = chat_completion.choices[0].message.content
    except Exception as e:
        ai_response = f"⚠️ Error: {str(e)}"

    return jsonify({"response": ai_response})
