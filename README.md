# Voice Bot
A simple voice-enabled chatbot using Openrouter Mistral AI API. Users can interact via text or voice, and the bot will generate responses as I would be responding to if some one ask about me otherwise it will give general response.

## Features
- Supports both text and voice input.
- Uses Mistral AI API for responses.
- Deployed on Render for public access.
- Interactive UI with a microphone button.

## Prerequisites
- Python 3.10.6 installed
- Git installed
- A Mistral AI API key

## Installation
### 1. Clone the repository:
   ```bash
   git clone https://github.com/Han9128/Voice-bot.git
   cd Voice-bot
   ```
### 2. Create and activate actual environment:
    ```bash
    python -m venv botenv
    source botenv/bin/activate  # On macOS/Linux
    botenv\Scripts\activate    # On Windows
    ```
### 3.Install dependencies:
```bash
pip install -r requirements.txt
```

### 4.Set up environment variables:
- Create a `.env` file in the root directory.
- Add your Mistral AI API key inside:
```bash
API_KEY=your_deepseek_api_key
```

### 5. Run the application:
```bash
python -m Backend.server
```




