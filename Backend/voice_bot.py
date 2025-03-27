import os
from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import time
from dotenv import load_dotenv
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
load_dotenv()  # Load .env file
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"  # OpenRouter API endpoint

# Initialize OpenAI (OpenRouter) client
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Read personal information from file
def load_personal_info(filename="myInfo.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Personal information file not found."

# Load personal info
personal_info = load_personal_info()
# print("Loaded personal info:", personal_info)
# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speaking speed

# -----------------------------
# FUNCTION TO CALL OpenRouter API
# -----------------------------
def ask_llm(question: str) -> str:
    try:
        # Define questions where the bot should introduce itself
        introduction_questions = [
            "what is your name",
            "who are you",
            "tell me about yourself",
            "introduce yourself"
        ]

        # Check if the question requires self-introduction
        if any(q in question.lower() for q in introduction_questions):
            system_message = f"""
                You are Md Shahreyar Hannan. Always introduce yourself when asked directly.
                Otherwise, answer questions normally based on the following details:
                
                {personal_info}
            """
        else:
            system_message = f"""
                Answer concisely using the following information when relevant:
                
                {personal_info}
            """

        response = client.chat.completions.create(
            model="mistralai/mistral-small-3.1-24b-instruct:free",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while connecting to the API: {e}"


# -----------------------------
# SPEECH RECOGNITION FUNCTION
# -----------------------------
def listen_for_question() -> str:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening... Please speak your question.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        question = recognizer.recognize_google(audio).lower()
        print("Detected question:", question)
        return question
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Speech Recognition error: {e}")
        return ""

# -----------------------------
# SPEECH SYNTHESIS FUNCTION
# -----------------------------
def speak_text(text: str):
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# MAIN LOOP
# -----------------------------
def main():
    print("Voice Bot is running. Ask your question (say 'exit', 'quit', or 'goodbye' to stop).")
    while True:
        question = listen_for_question()
        if not question:
            continue
        if question in ["exit", "quit", "goodbye"]:
            speak_text("Goodbye!")
            break

        answer = ask_llm(question)
        print("Answer:", answer)
        speak_text(answer)
        time.sleep(1)

if __name__ == "__main__":
    main()
