import os
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

# Wczytujemy klucz z pliku .env
load_dotenv()

app = Flask(__name__)

# Konfiguracja klienta Gemini
client = genai.Client()  # Klucz musi być w .env jako GEMINI_API_KEY


@app.route("/", methods=["GET", "POST"])
def home():
    odpowiedz = ""  # Domyślnie odpowiedź jest pusta

    if request.method == "POST":
        # 1. Pobieramy tekst z inputa (name="prompt")
        user_prompt = request.form.get("prompt")

        if user_prompt:
            try:
                # 2. Wysyłamy zapytanie do Gemini
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=user_prompt
                )
                # 3. Zapisujemy odpowiedź do zmiennej
                odpowiedz = response.text
            except Exception as e:
                odpowiedz = f"Wystąpił błąd: {e}"

    # 4. Przekazujemy odpowiedź (pustą lub z Gemini) do HTML
    return render_template("index.html", odpowiedz=odpowiedz)


if __name__ == '__main__':
    app.run(debug=True)

