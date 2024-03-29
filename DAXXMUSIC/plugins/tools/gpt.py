import time
import openai
import random
import requests
from DAXXMUSIC import app
from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ParseMode

# Set up OpenAI API credentials
openai.api_key = "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"

# Handler to process messages
@app.on_message(filters.command("ask"))
async def chat_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
      
        if len(message.command) < 2:
            bot.send_message(
                chat_id=message.chat.id,
                text="Example:\n\n/ask Where is TajMahal?"
            )
        else:
            question = message.text.split(' ', 1)[1]
            response = openai.Completion.create(
                engine="davinci",  # Use GPT-3 "davinci" model
                prompt=question,
                max_tokens=1000,  # Adjust the response length as needed
                n=1,
                stop=None,
                temperature=0.7,
            )

            answer = response.choices[0].text.strip()

            bot.send_message(
                chat_id=message.chat.id,
                text=f"{answer} Answer By @{BOT_USERNAME}",
                parse_mode=ParseMode.MARKDOWN
            )

    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Error: {str(e)}"
        )
