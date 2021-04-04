#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~ Bot name in Telegram @GestoFirstTestBot ~~~~~~~~~~~~~~

import telebot
import config
from telebot import types
import pandas as pd

bot = telebot.TeleBot(config.TOKEN)

MainFile = pd.read_csv('AllDatas.csv', low_memory=False)    #Your file with data
MainFile = MainFile.sort_values(by="d_reg")

def searcher(value):
    search_value = value
    search_value = search_value.upper()
    answer_value = MainFile[MainFile['n_reg_new'].isin([search_value])]
    answer_value = answer_value.iloc[:, 1:6]
    lll= answer_value.iloc[:, 1:2]
    lol=len(lll)
    finn_mess = ""
    for i in range(lol):
        standart_message = "Реєстрація:     {0}\nМарка:             {1}\nМодель:          {2}\nРік випуску:   {3}\nКолір:                {4}\n~~~~~~~~~~~~~~~~\n"

        dr=answer_value.iloc[i,0]
        mr=answer_value.iloc[i,1]
        md=answer_value.iloc[i,2]
        ye=answer_value.iloc[i, 3]
        co=answer_value.iloc[i, 4]
        alt_mess = standart_message.format(dr, mr, md, ye, co)
        finn_mess=finn_mess+alt_mess
    alt_mess=finn_mess

    print(alt_mess)

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
