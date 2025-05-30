import requests
import time

ENDPOINT = "https://telegram-template-bot.onrender.com/health"

def main():
    ts = int(time.time())
    url = f"{ENDPOINT}?ts={ts}"
    resp = requests.get(url)
    print(f"Pinged {url} - HTTP {resp.status_code}")

if __name__ == "__main__":
    main()
