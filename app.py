
import logging
from googletrans import Translator
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

translator = Translator()

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Translator Bot! Send me a message and I will translate it. Use /translate  to translate.')

def translate_text(update: Update, context: CallbackContext) -> None:
    # Get the text from the incoming message
    text_to_translate = update.message.text
    dest_language = 'en'  # Default destination language

    # Check for language code in the command arguments
    if len(context.args) > 0:
        dest_language = context.args[0]  # Get the language code from user input

    try:
        translated = translator.translate(text_to_translate, dest=dest_language)
        update.message.reply_text(f'Translated Text: {translated.text}')
    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}')

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("8117827824:AAF6JuMOTeZd-Y_vuUsaRIE5lctvZYOfvPU")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
