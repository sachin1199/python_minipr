import pyttsx3
import speech_recognition as sr
import json

# Load configuration
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

config = load_config()

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', config.get("speech_rate", 170))
engine.setProperty('volume', config.get("volume", 1.0))

# Global flag for speech mode
speech_enabled = True  # Default: voice on

def set_speech_mode(mode: bool):
    """Enable or disable speech output."""
    global speech_enabled
    speech_enabled = mode
    print(f"Speech mode set to: {'ON' if speech_enabled else 'OFF'}")

def speak(text: str):
    """Speaks text only if speech mode is enabled, always prints it."""
    print(f"{config.get('assistant_name', 'Assistant')}: {text}")
    if speech_enabled:
        engine.say(text)
        engine.runAndWait()
    return text

def listen():
    """Captures microphone input and returns recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't catch that.")
        return ""
