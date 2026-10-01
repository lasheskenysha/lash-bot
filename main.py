import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для наращивания ресниц 💕\nВыбери нужный раздел в меню.")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Прайс-лист:\nКлассика — 2000₽\n2D — 2500₽\n3D — 3000₽")

async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Запись: отправь своё имя, телефон и удобную дату.")

async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 Подарок: приведи подругу — скидка 20% на первое наращивание!")

async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Акции: скидка 15% на первое посещение.")

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Связаться: @your_instagram\nТелефон: +7 XXX XXX-XX-XX")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("book", book))
app.add_handler(CommandHandler("gift", gift))
app.add_handler(CommandHandler("promo", promo))
app.add_handler(CommandHandler("contacts", contacts))

app.run_polling()
