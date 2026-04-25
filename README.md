<img width="567" height="183" alt="image" src="https://github.com/user-attachments/assets/5189fa85-818d-451b-b3e5-165996e74756" />



# 🤖 Gemini AI Chat App

Nowoczesna aplikacja webowa typu Chat, integrująca model **Google Gemini AI** z frameworkiem **Flask**. Interfejs został zaprojektowany w stylu "Dark Mode" inspirowanym wyszukiwarką Google.

---

## 📋 Spis treści
1. [Funkcje](#-funkcje)
2. [Technologie](#-technologie)
3. [Instalacja](#-instalacja)
4. [Konfiguracja](#-konfiguracja)
5. [Struktura projektu](#-struktura-projektu)

---

## ✨ Funkcje
* **Minimalistyczny Design:** Estetyczny pasek wyszukiwania w trybie ciemnym.
* **Interaktywność:** Animacja pulsujących kropek (loader) sygnalizująca oczekiwanie na odpowiedź AI.
* **Stabilność:** Obsługa błędów serwera (np. błąd 503 UNAVAILABLE).
* **Single-file Logic:** Możliwość uruchomienia całej aplikacji z jednego pliku Python.

## 🚀 Technologie
* **Backend:** Python 3.x / Flask
* **AI SDK:** `google-genai` (Model: `gemini-3-flash-preview`)
* **Frontend:** HTML5, CSS3, JavaScript
* **Zmienne środowiskowe:** `python-dotenv`

## 🛠️ Instalacja

1. **Pobierz projekt:**
   ```bash
   git clone https://github.com/przemekstankiewiczpl-spec/Chat_25_04_2026.git
   cd nazwa-projektu
Przygotuj środowisko:

Bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows

Zainstaluj biblioteki:

Bash
pip install flask google-genai python-dotenv

⚙️ Konfiguracja

Stwórz plik .env w głównym katalogu projektu i wklej swój klucz API:

Fragment kodu
GEMINI_API_KEY=TwojKluczZGoogleAIStudio

🖥️ Uruchomienie

Uruchom aplikację komendą:

Bash
python app.py
Następnie otwórz przeglądarkę i wejdź na: http://127.0.0.1:5000
