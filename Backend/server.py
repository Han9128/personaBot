from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from voice_bot import ask_llm  # Import your existing function

# Initialize Flask app
app = Flask(__name__)
# public_url = ngrok.connect(5000).public_url
# print(f"Your chatbot is live at: {public_url}")
# Serve UI
@app.route("/")
def index():
    return render_template("index.html")  # UI serve karega

# API route to get chatbot response
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "Please ask a question."})

    answer = ask_llm(user_input)  # Using your existing function
    return jsonify({"response": answer})

# Run Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
