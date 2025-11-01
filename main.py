from flask import Flask, render_template, request, jsonify
from ai_logic import process_command, stop_current_task
from utils import set_speech_mode

app = Flask(__name__)

speech_mode = True  # default voice on

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")
    mode = data.get("mode", "voice")  # voice or text

    speech = True if mode == "voice" else False
    set_speech_mode(speech)
    reply = process_command(user_message, speech_mode=speech)

    return jsonify({"reply": reply})

@app.route("/stop", methods=["POST"])
def stop():
    stop_current_task()
    return jsonify({"reply": "Stopped current task."})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render dynamically assigns a port
    app.run(host="0.0.0.0", port=port)
