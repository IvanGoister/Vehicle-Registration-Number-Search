#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~ Bot name in Telegram @GestoFirstTestBot ~~~~~~~~~~~~~~

import telebot
import config
from telebot import types
import pandas as pd

bot = telebot.TeleBot(config.TOKEN)


BigSortedData = pd.read_csv('BigSortedData.csv', low_memory=False)

def searcher(value):
    search_value = value.upper()
    answer_value = BigSortedData[BigSortedData['N_REG_NEW'].isin([search_value])]
    answer_value = answer_value.loc[:,['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'N_REG_NEW']]

    for a in range(len(answer_value)):
        ff = answer_value.iloc[a, 0]
        if ff[4] == '-':
            alt_date_format = ff[8:] + '.' + ff[5:7] + '.' + ff[0:4]
            answer_value.iloc[a, 0] = alt_date_format
        else:
            pass
        
    print(answer_value["D_REG"])

    print(answer_value)
    finn_mess = ""
    for i in range(len(answer_value)):

        standart_message = "Реєстрація:     {0}\nМарка:             {1}\nМодель:          {2}\nРік випуску:   {3}\nКолір:                {4}\n~~~~~~~~~~~~~~~~\n"

        dr = answer_value.iloc[i, 0]
        mr = answer_value.iloc[i, 1]
        md = answer_value.iloc[i, 2]
        ye = answer_value.iloc[i, 3]
        co = answer_value.iloc[i, 4]

        alt_mess = standart_message.format(dr, mr, md, ye, co)
        finn_mess=finn_mess+alt_mess
    alt_mess=finn_mess

    return alt_mess


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вимоги до пошуку")
    item2 = types.KeyboardButton("Button 2")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Тестовий бот для отримання інформації по номерному знаку автомобіля".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':

        if message.text == 'Вимоги до пошуку':
            bot.send_message(message.chat.id, str('Написати номерний знак автомобіля українськими літареми і без пробілів'))
        elif message.text == 'Button 2':
            bot.send_message(message.chat.id, str('Button 2 working'))
        elif message.text == True:
            bot.send_message(message.chat.id, str('Інформація про номерний знак в базі відсутня'))
        else:
            bot.send_message(message.chat.id, str('Шукаю номерний знак %s ' % message.text))
            print(message.text)
            answer = searcher(message.text)

            if answer == "":
                bot.send_message(message.chat.id, str('Інформація про номерний знак в базі відсутня'))
                print("Номерний знак в базі відсутній")
            else:
                bot.send_message(message.chat.id, message.text)
                bot.send_message(message.chat.id, str(answer))


#RUN
bot.polling(none_stop=True)

