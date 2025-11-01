# AI Assistant (Python Mini Project)

##  Features

✅ **Voice and Text Modes** – Choose between speaking to the assistant or typing your commands.  
✅ **Wikipedia Search** – Fetches summarized information using the `wikipedia` API.  
✅ **Tell Jokes** – Uses the `pyjokes` library for humor.  
✅ **Time Reporting** – Announces the current system time.  
✅ **Web Automation** – Opens YouTube or other predefined sites on command.  
✅ **Task Control** – Stop ongoing tasks anytime using `/stop` endpoint.  
✅ **Flask Web Interface** – Interactive web-based frontend.  
✅ **Speech Toggle** – Enable or disable voice output dynamically.

---

## Tech Stack

- **Python 3.x**
- **Flask** (for web server and API endpoints)
- **SpeechRecognition** (for capturing and interpreting voice)
- **pyttsx3** (for text-to-speech)
- **pyjokes** (for jokes)
- **wikipedia** (for fetching summaries)
- **HTML/CSS/JS** (for frontend interface)

---

##  Project Structure
```
python_project/
│
├── main.py # Flask app entry point
├── ai_logic.py # Core AI logic & command handling
├── utils.py # Speech and utility functions
├── config.json # Configuration for voice rate, name, etc.
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Web interface
└── pycache/ # Cached Python files (auto-generated)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
https://github.com/sachin1199/python_minipr.git
cd python_project
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```

3️⃣ Run the project
```
python main.py
```

Example Commands
| Command                   | Description              |
| ------------------------- | ------------------------ |
| "What is AI on Wikipedia" | Fetches summary about AI |
| "Tell me a joke"          | Says a random joke       |
| "What’s the time"         | Speaks current time      |
| "Open YouTube"            | Opens YouTube in browser |
| "Stop"                    | Stops the current task   |
| "Hello"                   | Greets you back          |



How It Works

Frontend (index.html) – Sends user input (voice/text) to Flask backend via /ask.

Backend (Flask) – Receives command → passes it to ai_logic.py.

AI Logic – Parses the command, decides the intent, and executes the correct function (e.g., Wikipedia search, joke, etc.).

Speech Mode (utils.py) – Handles whether to speak out the response using pyttsx3.

Response – The processed output is displayed on the web UI and optionally spoken aloud.


Example Output

User: “Tell me a joke.”
Assistant: “Why did the developer go broke? Because he used up all his cache!” 😄

User: “What is machine learning on Wikipedia?”
Assistant: “Machine learning is a branch of artificial intelligence that focuses on building systems that can learn from data...”

Author

Developed by: Sachin Singh
Course: MCA (Data Science)
Mini Project Title: AI Assistant


