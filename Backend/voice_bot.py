import os
from openai import OpenAI
import speech_recognition as sr
from gtts import gTTS  # Importing gTTS for text-to-speech
import time
from dotenv import load_dotenv
import io
import pygame  # To play the audio directly from memory

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
        
        # Define greetings
        greetings = ["hi", "hello", "hey", "greetings", "good morning", "good evening"]

        # Check if the question requires self-introduction
        if any(q in question.lower() for q in introduction_questions):
            system_message = f"""
                You are Md Shahreyar Hannan. Always introduce yourself when asked directly.
                Otherwise, answer questions normally based on the following details:
                
                {personal_info}
            """
        elif any(greet in question.lower() for greet in greetings):
            return "Hello! How can I help you today?"  # Respond with a greeting
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
            answer = response.choices[0].message.content
            
            # If the response is empty, return a default message
            if not answer:
                return "Sorry, I couldn't provide an answer. Please try again."

            return answer
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
# SPEECH SYNTHESIS FUNCTION USING gTTS
# -----------------------------
def speak_text(text: str, lang='en'):
    if not text:
        print("No text to speak. Exiting.")
        return  # Exit if there's no text to speak
    
    tts = gTTS(text=text, lang=lang, slow=False)  # Convert text to speech
    fp = io.BytesIO()
    tts.write_to_fp(fp)  # Write the speech to the byte stream instead of saving to a file
    fp.seek(0)

    # Initialize pygame mixer to play the byte stream directly
    pygame.mixer.init()
    pygame.mixer.music.load(fp, 'mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


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
        elif any(greeting in question for greeting in ["hi", "hello", "hey", "greetings"]):
            speak_text("Hello! How can I help you today?", lang='en')
            continue  # Skip processing the rest of the question

        answer = ask_llm(question)
        print("Answer:", answer)
        speak_text(answer)
        time.sleep(1)

if __name__ == "__main__":
    main()
