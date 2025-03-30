# personaBot
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
#### On macOS/Linux
```bash
python -m venv botenv
source botenv/bin/activate
```
#### On Windows  
```bash
python -m venv botenv
botenv\Scripts\activate    
```
### 3.Install dependencies:
```bash
pip install -r requirements.txt
```

### 4.Set up environment variables:
- Create a `.env` file in the root directory.
- Add your Mistral AI API key inside:
```bash
API_KEY=your_MistralAI_API_key
```

### 5. Run the application:
```bash
python -m Backend.server
```
## Usage
1. Open the deployed web app.
2. Click the microphone button and speak your query.
3. The bot will process your voice and respond accordingly.
4. You can also type queries manually in the text box.

## Deployment
To deploy this bot on Render:
1. Push your code to GitHub.
2. Create a **Web Service** on [Render](https://render.com).
3. Set up environment variables (API_KEY).
4. Use `pip install -r requirements.txt` as the build command.
5. Use `python -m Backend.server` as the start command.
6. Deploy and test your bot.

## Live Demo
Try it here: [personaBot](https://voice-bot-2-vx9e.onrender.com/).

## Technologies Used  
This project was built using the following technologies:  
- **Flask** – Python web framework for handling backend logic  
- **JavaScript** – Handles frontend interactions  
- **HTML & CSS** – UI design and styling  
- **Mistral AI API** – AI model powering chatbot responses  

## Contributing  
Contributions are welcome! If you'd like to improve this project:  
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push the branch (`git push origin feature-branch`)  
5. Open a pull request  

For major changes, please open an issue first to discuss your proposal.  

## License  
This project is licensed under two options:

1. **Open Source License (MIT)** – Free for personal and non-commercial use.
2. **Commercial License** – Required for commercial use.

Commercial use, including but not limited to selling, licensing, or distributing this software as part of a paid product/service, **is strictly prohibited without explicit permission** from the author.

See the [LICENSE](LICENSE) file for more details.

For commercial licensing inquiries, contact mdshahreyarhannan@gmail.com.
 

## Contact  
For any queries or collaboration opportunities, feel free to reach out:  
📧 **Email:** mdshahreyarhannan@gmail.com  
🔗 **GitHub:** [Han9128](https://github.com/Han9128)  






