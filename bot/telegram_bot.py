import os
from dotenv import load_dotenv

load_dotenv()

from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging

from transcribe.whisper_transcribe import transcribe_file

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Ciao {update.effective_user.first_name}, sono un bot scritto da Marco che trascrive i messaggi vocali mandati da questa chat, utilizzando OpenAI Whisper. Nessun file è salvato in locale o in cloud.",
    )

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.voice.duration > 30:
        logger.info(f"Vocale ricevuto da {update.effective_user.first_name}. Durata (s): {update.message.voice.duration}.")
        pass
    file = await context.bot.get_file(update.message.voice.file_id)
    audio_data = await file.download_to_drive()
    testo = transcribe_file(audio_data.name)
    logger.info(f"Vocale ricevuto da {update.effective_user.first_name}. Durata (s): {update.message.voice.duration}.  Testo: {testo}.")
    await update.message.reply_text(f"{update.effective_user.first_name} ha detto: {testo}.")
    os.remove(audio_data.name)

def run_bot():
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("info", info))
    application.add_handler(MessageHandler(filters.VOICE, voice_handler))
    application.add_error_handler(error)

    '''
    application.run_webhook(
        listen='0.0.0.0',
        port=os.getenv("WEBHOOK_PORT"),
        url_path=TOKEN,
        webhook_url=f"os.getenv("WEBHOOK_URL")/{TOKEN}")
    '''

    application.run_polling()

if __name__ == '__main__':
    run_bot()