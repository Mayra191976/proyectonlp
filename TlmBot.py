# -*- coding: utf-8 -*-
# se añade @BotFather en telegran
# se le manda el comando: /start
# se le manda el comando: /newbot

import telebot
import time

# NlpYoutubebot 
bot = telebot.TeleBot("5810350735:AAEo6vldLg1J_RzMRgGBugDpoFePB_EDWuQ")

# Comandos.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Hola")
# echo

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    time.sleep(3)
    print(message.text)
    if message.text.find("A") >= 0:
        bot.reply_to(message, "12346")

bot.polling()