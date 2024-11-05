

# Replace these with your own credentials





# Replace these with your own credentials

import os
import pyrogram
from pyrogram import Client, filters
from googletrans import Translator

# Replace with your bot token and API ID/HASH


# Create a Pyrogram client

API_ID = "10247139"
API_HASH = "96b46175824223a33737657ab943fd6a"
BOT_TOKEN = "8117827824:AAHmkbcHHyYTldbgwOHsLMlR7D9Xrzihvvw"
# Initialize the Google Translate translator
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
translator = Translator()

@app.on_message(filters.command(["translate", "tr"]))
async def translate_text(client, message):
    """Translates the provided text to the specified language."""

    try:
        # Extract the language code and text from the message
        args = message.text.split()[1:]
        if len(args) < 2:
            await message.reply("Please provide the target language code and text to translate.")
            return

        target_language = args[0]
        text_to_translate = " ".join(args[1:])

        # Translate the text
        translation = translator.translate(text_to_translate, dest=target_language)

        # Send the translated text
        await message.reply(f"*Translation to {target_language}:*\n{translation.text}")

    except Exception as e:
        await message.reply(f"An error occurred: {e}")


app.run() 

