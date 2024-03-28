from pyrogram import Client, filters
import openai
from DAXXMUSIC import app


# Set up OpenAI API credentials
openai.api_key = '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'


# Handler to process messages
@app.on_message(filters.group)
def handle_message(client, message):
    chat_id = message.chat.id
    text = message.text

    # Call OpenAI API for text completion
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=50  # Adjust the response length as needed
    )

    reply = response.choices[0].text.strip()

    client.send_message(chat_id, reply)


# Main function to run the bot
def main():
    app.run()


if __name__ == '__main__':
    main()
