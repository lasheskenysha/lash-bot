import os
import time
import requests

TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    try:
        r = requests.get(url, params=params, timeout=35)
        return r.json()
    except:
        return {"ok": False}

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if updates.get("ok"):
            for update in updates.get("result", []):
                last_update_id = update["update_id"] + 1
                message = update.get("message", {})
                text = message.get("text", "")
                chat_id = message.get("chat", {}).get("id")
                if not chat_id:
                    continue
                if text == "/start":
                    send_message(chat_id, "Привет! Я бот Алины по наращиванию ресниц 💕")
                elif text == "/price":
                    send_message(chat_id, "Классика — 1700\n2D — 1900\n3D — 2000\n4-10D — от 2500\nЦветные +300\nСнятие 300")
                elif text == "/book":
                    send_message(chat_id, "Напишите мне: @Kernysha или позвоните: 89118198643")
                elif text == "/gift":
                    send_message(chat_id, "Бонус 500₽ на любую услугу! Действует 7 дней 🎁")
                elif text == "/promo":
                    send_message(chat_id, "Первое посещение — скидка 10%\nПриведи подругу — скидка 15%")
                elif text == "/contacts":
                    send_message(chat_id, "Telegram: @Kernysha\nТелефон: 89118198643\nАдрес: Шушары, Новгородский пр. 8")
        time.sleep(1)

if __name__ == "__main__":
    main()
