import os
import pty
import subprocess
import threading
import eventlet
import datetime
import re
import signal
import time
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO

eventlet.monkey_patch()

# Récupérer le mot de passe et la clé secrète
PASSWORD = ""
SECRET_KEY = os.urandom(16)  # Clé secrète pour Flask

app = Flask(__name__)
app.secret_key = SECRET_KEY
socketio = SocketIO(app, cors_allowed_origins="*")

LOG_DIR = "logs"
HISTORY_FILE = os.path.join(LOG_DIR, "session_history.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

bot_process = None  # Stocke le processus du bot

# Nettoyer les séquences ANSI pour éviter les problèmes d'affichage
def clean_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

# Sauvegarde une ligne dans l'historique
def save_to_history(text):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(text + "\n")

# Charger l'historique de la session précédente
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return ""

# Lancer un terminal interactif avec un prompt propre
master, slave = pty.openpty()
shell = subprocess.Popen(
    ["bash", "--norc", "--noediting", "-i"],
    stdin=slave,
    stdout=slave,
    stderr=slave,
    preexec_fn=os.setsid,
    text=True,
    bufsize=1,
    universal_newlines=True,
    env={"PS1": "\\u@\\h:\\w$ "}  # ✅ Définition propre du prompt
)

def read_from_terminal():
    """ Lit les sorties du shell, nettoie les codes ANSI et envoie au WebSocket """
    while True:
        try:
            output = os.read(master, 1024).decode("utf-8")
            clean_output = clean_ansi_codes(output)
            save_to_history(clean_output)  # ✅ Sauvegarde aussi la sortie du terminal
            socketio.emit("log", clean_output)
        except OSError:
            break

# Thread pour écouter les sorties du shell
threading.Thread(target=read_from_terminal, daemon=True).start()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        submit_time = int(request.form.get("timestamp", 0))
        current_time = int(time.time())

        # Vérification que le formulaire a été soumis dans les 5 secondes
        if current_time - submit_time > 5:
            return redirect(url_for("login"))

        # Authentification réussie, rediriger vers la console
        return redirect(url_for("console"))

    return render_template("login.html", timestamp=int(time.time()))

@app.route("/console")
def console():
    history = load_history()  # ✅ Charger tout l'historique de la session
    return render_template("console.html", history=history)

@socketio.on("send_command")
def send_command(cmd):
    os.write(master, (cmd + "\n").encode("utf-8"))
    save_to_history(f"> {cmd}")  # ✅ Sauvegarde aussi la commande tapée

@socketio.on("ctrl_c")
def send_ctrl_c():
    """ Envoie un SIGINT (équivalent de Ctrl + C) au processus en avant-plan """
    os.killpg(os.getpgid(shell.pid), signal.SIGINT)

@socketio.on("start_bot")
def start_bot():
    """ Démarre le bot Discord """
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(
            ["python3", "main.py"],  # Change le chemin si nécessaire
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        socketio.emit("log", "🚀 Bot Discord démarré !")

        def read_bot_output():
            for line in iter(bot_process.stdout.readline, ""):
                socketio.emit("log", line.strip())

        threading.Thread(target=read_bot_output, daemon=True).start()

@socketio.on("stop_bot")
def stop_bot():
    """ Arrête le bot Discord """
    global bot_process
    if bot_process:
        bot_process.terminate()
        bot_process = None
        socketio.emit("log", "❌ Bot Discord arrêté !")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
