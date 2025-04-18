import os
import telebot
from telebot import types
import requests


token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("ℹ️ How your question is processed")
    markup.add(btn1)

    welcome_text = (
        "👋 Hi! I'm a medical chatbot specialized in dermatology Q&A.\n\n"
        "💬 By sending a question, you agree that your message will be sent to:\n"
        "- 🧠 OpenAI (for language model processing)\n"
        "- 📦 Pinecone (to retrieve relevant medical context)\n"
        "- 🌐 Railway (which hosts the backend API)\n\n"
        "Your question is processed securely for educational use only."
    )

    bot.send_message(message.from_user.id, welcome_text, reply_markup = markup)


@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    FASTAPI_URL = 'https://fastapibackend-production-cd0e.up.railway.app/ask'
    if message.text == 'ℹ️ How your question is processed':
        info_text = (
            "🧾 Here's how your question is handled:\n\n"
            "1️⃣ Your message is sent to a backend service hosted on Railway.\n"
            "2️⃣ The backend queries Pinecone to retrieve relevant chunks from the dermatology textbook.\n"
            "3️⃣ The context + your question is sent to OpenAI's language model (GPT) to generate an answer.\n\n"
            "⚠️ Your question and related metadata may be processed by these services. "
            "No personal data is stored or shared."
        )
        bot.send_message(message.from_user.id, info_text)
    else:
        user_input = message.text
        try:
            response = requests.get(FASTAPI_URL, timeout = 5)
            print("PING STATUS:", response.status_code)
            print("PING TEXT:", response.text)
        except Exception as e:
            print(f"❌ Ping failed: {e}")
        
        try:
            response = requests.post(FASTAPI_URL, json={"question": user_input}, timeout = 10)
            print("STATUS:", response.status_code)
            print("TEXT:", response.text)
            response.raise_for_status()
            answer = response.json().get("answer", "🤖 No answer returned.")
        except Exception as e:
            answer = f"❌ Bot Error: {e}"
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True, interval = 0)

