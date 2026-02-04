import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        },
        timeout=10
    )

if __name__ == "__main__":
    send("🟢 Captain Wealth Bot is LIVE (GitHub repo test)")
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print("Status:", r.status_code)
    print(r.text)

send("🚀 Captain Wealth Bot is LIVE (GitHub Actions test)")
