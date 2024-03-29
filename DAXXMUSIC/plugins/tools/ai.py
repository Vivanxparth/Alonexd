import random
import time
import requests
from DAXXMUSIC import app
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

BUTTON = InlineKeyboardMarkup(
       [
              [
                     InlineKeyboardButton(
                            text=f"〆 ᴄʟᴏsᴇ 〆",
                            callback_data="close",
                    )
              ]
       ]
)              

@app.on_message(filters.command(["chatgpt","ai","ask","gpt"],  prefixes=["+", ".", "/", "", "$","&"]))
async def zzchat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n/ai How To Set Girlfriend? "
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                # Check if "results" key is present in the JSON response
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f" {x} ✨",
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=BUTTON
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
