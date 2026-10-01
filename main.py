import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот мастера по наращиванию ресниц Алины 💕\n\n"
        "Предлагаю качественное наращивание ресниц в Шушарах. Работаю на премиальных материалах, "
        "безопасно и стерильно. Подбираю изгиб, длину и объём индивидуально под ваш тип глаз.\n\n"
        "Выбери нужный раздел в меню 👇"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Прайс-лист:\n\n"
        "Классика — 1700₽\n"
        "2D — 1900₽\n"
        "3D — 2000₽\n"
        "4-10D — от 2500₽\n"
        "Цветные ресницы — +300₽\n"
        "Снятие ресниц (не мои работы) — 300₽"
    )

async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Запись:\n\n"
        "Напишите мне в Telegram @Kernysha или позвоните: +7 911 819-86-43 — подберу удобное время 💕"
    )

async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎁 Подарок!\n\n"
        "Внутри — бонус 500₽ на любую услугу по наращиванию ресниц.\n"
        "Отличный повод попробовать тот самый объём или цвет из сохранёнок ✨\n\n"
        "Подарок действует 7 дней.\n"
        "Подобрать вам окошко в будни или на выходных?"
    )

async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Акции:\n\n"
        "Первое посещение — скидка 10%\n"
        "Приведи подругу — скидка 15% на следующую процедуру"
    )

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Связаться со мной:\n\n"
        "Telegram: @Kernysha\n"
        "Телефон: +7 911 819-86-43\n"
        "Instagram: https://www.instagram.com/lashes_kernysh\n"
        "Авито: https://www.avito.ru/sankt-peterburg/predlozheniya_uslug/naraschivanie_resnits_8513239570\n\n"
        "📍 Адрес: Шушары, Новгородский проспект 8"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("book", book))
    app.add_handler(CommandHandler("gift", gift))
    app.add_handler(CommandHandler("promo", promo))
    app.add_handler(CommandHandler("contacts", contacts))
    app.run_polling()

if __name__ == "__main__":
    main()
