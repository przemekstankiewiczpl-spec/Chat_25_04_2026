import json
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

# Wczytujemy klucz z pliku .env
load_dotenv()

app = Flask(__name__)

# Konfiguracja klienta Gemini
client = genai.Client()  # Klucz musi być w .env jako GEMINI_API_KEY
# history = []

@app.route("/", methods=["GET", "POST"])
def home():
    odpowiedz = ""
    history = []  # Inicjalizacja pustej listy dla metody GET

    if request.method == "POST":
        # 1. Pobieramy poprzednią historię z ukrytego pola w HTML
        history_raw = request.form.get("history", "[]")
        history = json.loads(history_raw)

        # 2. Pobieramy pytanie użytkownika
        user_prompt = request.form.get("prompt")

        if user_prompt:
            # Dodajemy pytanie użytkownika do historii przed wysłaniem
            history.append({"role": "user", "parts": [{"text": user_prompt}]})

            try:
                # 3. Wysyłamy całą historię do Gemini
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=history
                )
                odpowiedz = response.text

                # KLUCZOWY MOMENT: Dodajemy odpowiedź modelu do historii
                history.append({"role": "model", "parts": [{"text": odpowiedz}]})

            except Exception as e:
                odpowiedz = f"Wystąpił błąd: {e}"

    # 4. Przekazujemy zaktualizowaną historię (z pytaniem i odpowiedzią!) do HTML
    return render_template("index.html", odpowiedz=odpowiedz, history=json.dumps(history))


if __name__ == '__main__':
    app.run(debug=True)

