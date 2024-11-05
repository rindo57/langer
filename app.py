
from pyrogram import Client, filters
from googletrans import Translator

# Replace these with your own credentials
API_ID = "10247139"
API_HASH = "96b46175824223a33737657ab943fd6a"
BOT_TOKEN = "8117827824:AAHmkbcHHyYTldbgwOHsLMlR7D9Xrzihvvw"

app = Client("translator_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

translator = Translator()

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Welcome to the Translator Bot! Send me a message to translate.")

@app.on_message(filters.text & ~filters.command)
def translate_text(client, message):
    text_to_translate = message.text
    dest_language = 'en'  # Default destination language

    # Check if the first word in the message is a language code
    words = text_to_translate.split()
    if words:
        # Check if the first word is a valid language code
        if len(words[0]) == 2:  # Assuming language codes are 2 characters long
            dest_language = words[0]
            text_to_translate = ' '.join(words[1:])  # Remove the language code from the text

    try:
        translated = translator.translate(text_to_translate, dest=dest_language)
        message.reply_text(f'Translated Text: {translated.text}')
    except Exception as e:
        message.reply_text(f'Error: {str(e)}')

if __name__ == "__main__":
    app.run()
