import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот Алины по наращиванию ресниц 💕")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Классика — 1700\n2D — 1900\n3D — 2000\n4-10D — от 2500\nЦветные +300\nСнятие 300")

async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напишите мне: @Kernysha или позвоните: 89118198643")

async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бонус 500₽ на любую услугу! Действует 7 дней 🎁")

async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Первое посещение — скидка 10%\nПриведи подругу — скидка 15%")

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Telegram: @Kernysha\nТелефон: 89118198643\nInstagram: lashes_kernysh\nАдрес: Шушары, Новгородский пр. 8")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("book", book))
app.add_handler(CommandHandler("gift", gift))
app.add_handler(CommandHandler("promo", promo))
app.add_handler(CommandHandler("contacts", contacts))

app.run_polling()
