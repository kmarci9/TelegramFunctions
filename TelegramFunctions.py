# Coding UTF-8
# Created by: kmarci9 2017.10.08
# Using this module https://github.com/python-telegram-bot/python-telegram-bot 
# Or use pip :    pip install python-telegram-bot


import telegram
from telegram.ext import Updater, CommandHandler
import sys
import os
import time
from ConfigParameters import *

def ReadBotToken():
    # A Bot API tokenjet kulso fajlbol olvassa be
    token_file = open("telegram_bot_api.txt")
    token = token_file.read()
    return token

token = ReadBotToken()
chat_id = "-263284135" #A csoportunk ID-je 
bot = telegram.Bot(token=token)
updater = Updater(token)
j = updater.job_queue
localtime = time.localtime()


def Sell_Notification( balance,currentSellingPrice,base_currency):
    if CONFIGEnable_Telegram_Notifications == True:
        bot.send_message(chat_id=chat_id,text=time.strftime('%Y/%m/%d/%H:%M:%S',localtime) + "\n\n" + "Eladott " \
                         + str(base_currency) + "\nIlyen arfolyamon " + str(currentSellingPrice) + "\n" + "<b>Jelenlegi egyenleg " + str(balance) + " " + str(base_currency) + "</b>" \
                         ,parse_mode=telegram.ParseMode.HTML)

def Buy_Notification(balance,currentBuyingPrice,base_currency):
    if CONFIGEnable_Telegram_Notifications == True:
        bot.send_message(chat_id=chat_id,text=time.strftime('%Y/%m/%d/%H:%M:%S',localtime) + "\n\n" + "Vett " \
                         + str(base_currency) + "\nIlyen arfolyamon " + str(currentBuyingPrice) + "\n" + "<b>Jelenlegi egyenleg " + str(balance) + " " + str(base_currency) + "</b>" \
                         ,parse_mode=telegram.ParseMode.HTML)
