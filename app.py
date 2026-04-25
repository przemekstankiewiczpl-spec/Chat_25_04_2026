import json
import os
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

# Wczytujemy klucz z pliku .env
load_dotenv()

app = Flask(__name__)

# Konfiguracja klienta Gemini
client = genai.Client()

@app.route("/", methods=["GET", "POST"])
def home():
    odpowiedz = ""
    history = []  # Pusta lista na start (dla GET)

    if request.method == "POST":
        # 1. Pobieramy tekst z inputów
        user_prompt = request.form.get("prompt")
        history_raw = request.form.get("history")

        # 2. Bezpieczne parsowanie JSON
        if history_raw:
            try:
                history = json.loads(history_raw)
            except (json.JSONDecodeError, TypeError):
                history = []
        else:
            history = []

        if user_prompt:
            # Dodajemy pytanie użytkownika
            history.append({"role": "user", "parts": [{"text": user_prompt}]})

            try:
                # 3. Wysyłamy zapytanie (zmień model na 1.5-flash jeśli 3-preview znów przekroczy limity)
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=history
                )
                odpowiedz = response.text

                # Dodajemy odpowiedź modelu do historii
                history.append({"role": "model", "parts": [{"text": odpowiedz}]})

            except Exception as e:
                # Jeśli wystąpi błąd API (np. limit 429), usuwamy ostatnie pytanie użytkownika,
                # żeby nie dublowało się przy ponownej próbie
                if history:
                    history.pop()
                odpowiedz = f"Wystąpił błąd: {e}"

    # 4. Przekazujemy dane do szablonu
    return render_template(
        "index.html",
        odpowiedz=odpowiedz,
        history_list=history,           # Do pętli {% for %}
        history_json=json.dumps(history) # Do input type="hidden"
    )

if __name__ == '__main__':
    app.run(debug=True)