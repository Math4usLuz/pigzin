from flask import Flask
import requests
from threading import Thread
import time

app = Flask(__name__)

# Coloque o link do seu bot/keep_alive no Replit
BOT_URL = "https://seu-repl-link.repl.co/"  

def ping_bot():
    while True:
        try:
            r = requests.get(BOT_URL)
            print(f"Ping enviado! Status: {r.status_code}")
        except Exception as e:
            print(f"Erro ao pingar o bot: {e}")
        time.sleep(60)  # ping a cada 1 minuto

# Rodar ping em background
Thread(target=ping_bot, daemon=True).start()

@app.route("/")
def home():
    return "API de ping rodando!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
