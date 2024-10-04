import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM-KEY'])
global prevchat
prevchat = ""
your_user_id = int(os.environ['ID'])

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  chat = message.chat.id
  global prevchat
  if chat != prevchat:
    chat_info = bot.get_chat(chat)
    chat_name = chat_info.title
    chat_username = chat_info.username
    bot.send_message(your_user_id, f"Бот вступил в новый чат: {chat_name}")
    if chat_username:
      bot.send_message(your_user_id, f"Юзернейм чата: @{chat_username}")
    prevchat = chat
  while True:
    with open('text.txt', 'r', encoding='utf-8') as file:
      bot.send_message(message.chat.id, file.read())

bot.polling(non_stop=True, interval=0)