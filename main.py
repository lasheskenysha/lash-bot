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
        requests.post(f"{API}/sendMessage", json={"chat_id": chat_id, "text": text})
    except:
        pass

def main():
    last = None
    while True:
        data = get_updates(last)
        if data.get("ok"):
            for u in data.get("result", []):
                last = u["update_id"] + 1
                msg = u.get("message", {})
                text = msg.get("text", "")
                chat_id = msg.get("chat", {}).get("id")
                if not chat_id:
                    continue
                if text == "/start":
                    send(chat_id, "Привет! Я бот Алины по наращиванию ресниц 💕")
                elif text == "/price":
                    send(chat_id, "💰 Прайс-лист:\n\nКлассика — 1700₽\n2D — 1900₽\n3D — 2000₽\n4-10D — от 2500₽\nЦветные — +300₽\nСнятие (не мои работы) — 300₽")
                elif text == "/book":
                    send(chat_id, "📅 Запись:\n\nTelegram: @Kernysha\nТелефон: +7 911 819-86-43")
                elif text == "/gift":
                    send(chat_id, "🎁 Подарок!\n\nБонус 500₽ на любую услугу по наращиванию ресниц.\nДействует 7 дней ✨")
                elif text == "/promo":
                    send(chat_id, "🔥 Акции:\n\nПервое посещение — скидка 10%\nПриведи подругу — скидка 15%")
                elif text == "/contacts":
                    send(chat_id, "📞 Связаться:\n\nTelegram: @Kernysha\nТелефон: +7 911 819-86-43\nInstagram: lashes_kernysh\n📍 Шушары, Новгородский пр. 8")
        time.sleep(1)

if __name__ == "__main__":
    main()
