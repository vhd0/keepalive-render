from flask import Flask, redirect, request
import time

app = Flask(__name__)

@app.route("/ping")
def ping():
    ts = int(time.time())
    target_url = f"https://telegram-template-bot.onrender.com/health?ts={ts}"
    return redirect(target_url, code=302)

if __name__ == "__main__":
    app.run(port=8080)
