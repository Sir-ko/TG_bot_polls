import telebot
import deps
from commands import *

bot = telebot.TeleBot(deps.TOKEN)
commands_register(bot)
# @bot.message_handler(commands=['a'])
# def echo_message(message):
#     chat_id = message.chat.id
#     try:
#         msg_thread_id = message.reply_to_message.message_thread_id
#     except AttributeError:
#         msg_thread_id = "General"
#     bot.reply_to(message, f"Chat ID этого чата: {chat_id}\nИ message_thread_id: {msg_thread_id}")

if __name__ == '__main__':
    bot.infinity_polling()