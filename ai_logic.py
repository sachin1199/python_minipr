import wikipedia
import pyjokes
import datetime
import webbrowser
from utils import speak

stop_task = False  # global flag to interrupt ongoing work

def stop_current_task():
    global stop_task
    stop_task = True

def process_command(command, speech_mode=True):
    global stop_task
    stop_task = False  # reset before new command
    response = ""

    command = command.lower().strip()  # normalize input

    try:
        # --- STOP ---
        if "stop" in command:
            stop_current_task()
            response = "Task stopped."

        elif "hello" in command or "hi" in command:
          response = "Hello! How can I assist you today?"


        # --- TIME ---
        elif "time" in command:
            response = f"The time is {datetime.datetime.now().strftime('%H:%M')}."

        # --- JOKE ---
        elif "joke" in command:
            response = pyjokes.get_joke()

        # --- WIKIPEDIA ---
        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "").strip()
            if not topic:
                response = "Please tell me what to search on Wikipedia."
            else:
                try:
                    # 1️⃣ First attempt — normal fetch
                    response = wikipedia.summary(topic, sentences=2, auto_suggest=True)

                except wikipedia.PageError:
                    # 2️⃣ If page not found, try best search result
                    search_results = wikipedia.search(topic)
                    if search_results:
                        best_match = search_results[0]
                        try:
                            response = wikipedia.summary(best_match, sentences=2, auto_suggest=False)
                        except Exception as e:
                            response = f"I found '{best_match}', but couldn't fetch its details: {e}"
                    else:
                        response = "I couldn’t find any information on that topic."

                except wikipedia.DisambiguationError as e:
                    response = f"Your topic is too broad. Try one of these: {', '.join(e.options[:5])}."

                except Exception as e:
                    # 3️⃣ Catch network or parsing issues
                    if "HTTPSConnectionPool" in str(e) or "connection" in str(e).lower():
                        response = "I couldn’t connect to Wikipedia. Check your internet connection."
                    else:
                        response = f"Something went wrong while fetching from Wikipedia: {e}"

        # --- OPEN YOUTUBE ---
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            response = "Opening YouTube."

        # --- UNKNOWN COMMAND ---
        else:
            response = "Were you able to do that when you were one day old?"

    except Exception as e:
        response = f"An unexpected error occurred: {e}"

    if speech_mode:
        speak(response)

    return response
