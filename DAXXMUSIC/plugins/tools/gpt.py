import requests
from DAXXMUSIC import app as Mukesh
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from MukeshAPI import api
from config import BOT_NAME, BOT_USERNAME

@Mukesh.on_message(filters.command(["lol"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat_gpt(app, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/ask What is Chat Gpt?`")
        else:
            a = message.text.split(' ', 1)[1]
            r=api.chatgpt(a,mode="elonmusk")["results"]
            await message.reply_text(f" {r} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
