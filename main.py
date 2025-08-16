import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Ambil token dari Railway Environment Variables
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Contoh database ODP → koordinat
ODP_DATA = {
    "ODP001": "-6.558301,107.758095",
    "ODP002": "-6.560123,107.760456",
    "ODP003": "-6.561789,107.762111"
}

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim nomor ODP untuk melihat titik koordinatnya.")

# Handler pesan ODP
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().upper()
    if text in ODP_DATA:
        koordinat = ODP_DATA[text]
        maps_url = f"https://www.google.com/maps?q={koordinat}"
        await update.message.reply_text(f"📍 ODP {text}: {maps_url}")
    else:
        await update.message.reply_text("Nomor ODP tidak ditemukan di database.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot berjalan...")
    app.run_polling()
