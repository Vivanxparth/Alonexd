from pyrogram import Client, filters
import openai
from DAXXMUSUC import app

openai.api_key = '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'

@app.on_message(filters.command("heer") & filters.group)
def handle_message(client, message):
    chat_id = message.chat.id
    text = message.text

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=50  # Adjust the response length as needed
    )

    reply = response.choices[0].text.strip()

    client.send_message(chat_id, reply)
