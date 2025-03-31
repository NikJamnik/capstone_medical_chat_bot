import os
import telebot
from telebot import types
import requests


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("❓ Ask a question")
    btn2 = types.KeyboardButton("⚠️ Bot rules")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Hi! I'm medical chat bot specializied in dermatology QA!", reply_markup=markup)


@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    FASTAPI_URL = 'https://your-project-name.up.railway.app/ask'
    if message.text == '⚠️ Bot rules':
        bot.send_message(message.from_user.id, 'TODO: Add bot rules here')
    elif message.text == '❓ Ask a question':
        bot.send_message(message.from_user.id, 'You can write your question')
    else:
        user_input = message.text
        try:
            response = requests.post(FASTAPI_URL, json={"question": user_input}, timeout = 10)
            print("STATUS:", response.status_code)
            print("TEXT:", response.text)
            response.raise_for_status()
            answer = response.json().get("answer", "🤖 No answer returned.")
        except Exception as e:
            answer = f"❌ Bot Error: {e}"
        bot.send_message(message.chat.id, answer)


token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token)
bot.polling(none_stop = True, interval = 0)

