import os
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = genai.Client() # Klucz brany z .env (GEMINI_API_KEY)

@app.route("/", methods=["GET", "POST"])
def home():
    odpowiedz = ""
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        # Wywołanie Gemini z promptem od użytkownika
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=user_prompt
        )
        odpowiedz = response.text

    return render_template("index.html", odpowiedz=odpowiedz)

if __name__ == "__main__":
    app.run(debug=True)