from pyrogram import Client, filters
import transformers
from DAXXMUSIC import app

# Load pre-trained GPT-2 model
model_name = "gpt2"
tokenizer = transformers.GPT2Tokenizer.from_pretrained(model_name)
model = transformers.GPT2LMHeadModel.from_pretrained(model_name)

# Handler to process messages
@app.on_message(filters.command(["start", "help"]))
def start_command(client, message):
    reply = "Hello! I am an AI chatbot. You can start chatting with me by sending a message."
    client.send_message(message.chat.id, reply)


@app.on_message(~filters.command(["start", "help"]))
def handle_message(client, message):
    chat_id = message.chat.id
    text = message.text

    # Tokenize input
    inputs = tokenizer.encode(text, return_tensors="pt")

    # Generate response
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

    client.send_message(chat_id, reply)


# Main function to run the bot
def main():
    app.run()


if __name__ == '__main__':
    main()
