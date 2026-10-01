import os
import time
import requests

TOKEN = os.environ.get("TELEGRAM_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

def get_updates(offset=None):
    try:
        r = requests.get(f"{API}/getUpdates", params={"timeout": 30, "offset": offset}, timeout=35)
        return r.json()
    except:
        return {"ok": False}

def send(chat_id, text):
    try:
        requests.post(f"{
