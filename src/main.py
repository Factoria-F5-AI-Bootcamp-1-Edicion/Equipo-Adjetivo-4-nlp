# -*- coding: utf-8 -*-
# se añade @BotFather en telegran
# se le manda el comando: /start
# se le manda el comando: /newbot
import telebot
import time
from youtube import *
from ia import *
import os
from dotenv import load_dotenv
load_dotenv()
tlg = os.getenv('KEY_TLG')


# NlpYouTubeBot 
bot = telebot.TeleBot(tlg)

# Comandos.
@bot.message_handler(commands=['start', 'help', 'ayuda'])
def send_welcome(message):
      bot.reply_to(message, mensajes() )
      
      
print("¡Bot Arrancado!")
bot.polling()