import os
import threading
from flask import Flask

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "8395784175:AAEbCUtMNP892FjCk-o7Tn1CEIPCY4RFJfU"

web = Flask(__name__)

@web.route("/")
def home():
    return "ABDTEAM BOT WORKING"

pairs = [
    "AUD/CHF (OTC)",
    "USD/PHP (OTC)",
    "GBP/NZD (OTC)",
    "USD/BDT (OTC)",
    "EUR/CAD (OTC)",
    "USD/ARS (OTC)",
    "USD/CHF (OTC)",
    "GBP/JPY (OTC)",
    "NZD/CAD (OTC)",
    "EUR/CHF (OTC)",
    "USD/COP (OTC)",
    "USD/BRL (OTC)",
    "EUR/GBP (OTC)",
    "GBP/CAD (OTC)",
    "GBP/USD (OTC)",
    "NZD/JPY (OTC)",
    "USD/EGP (OTC)",
    "USD/JPY (OTC)",
    "USD/PKR (OTC)",
    "CAD/CHF (OTC)",
    "USD/IDR (OTC)",
    "EUR/AUD (OTC)",
    "EUR/USD (OTC)",
    "AUD/USD (OTC)",
    "AUD/CAD (OTC)",
    "AUD/JPY (OTC)",
    "CHF/JPY (OTC)"
]

times = ["1 Minute", "2 Minutes", "5 Minutes"]

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[p] for p in pairs]
    await update.message.reply_text(
        "🔥 Choose Trading Pair 🔥",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in pairs:
        users[update.effective_user.id] = {"pair": text}
        keyboard = [[t] for t in times]

        await update.message.reply_text(
            "⏰ Choose Time ⏰",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    
elif text in times:
        pair = users.get(update.effective_user.id, {}).get("pair", "EUR/USD 
if "last_trade" not in users:
                                                           if "last_trade" not in users:
    users["last_trade"] = "PUT ⬇️"

if users["last_trade"] == "CALL ⬆️":
    trade = "PUT ⬇️"
else:
    trade = "CALL ⬆️"

users["last_trade"] = trade

        signal = f"""
🔥 SIGNAL READY 🔥

PAIR: {pair}
TIME: {text}

TRADE: {trade}

🚀 GOOD LUCK 🚀
"""

        await update.message.reply_text(signal)

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("ABDTEAM SIGNALS BOT RUNNING...")
    app.run_polling()

    if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    run_bot()
