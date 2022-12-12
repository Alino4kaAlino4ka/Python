import time
import telebot
import datetime
import math


bot = telebot.TeleBot('5509668401:AAHILPtzjfmvskjXByAO7Pf6_hEASzzyeS4')
flag = 1


@bot.message_handler(commands=['start'])
def start_menu(message):
    bot.send_message(message.chat.id, text='''Приветствую, для узнавания даты используйте /date,
                                                для вычислений с рациональными числами/rational
                                                для вычислений с комплексными числамивниз /complex'''


def date(message):
    bot.send_message(message.chat.id, text=str(datetime.datetime.now())[0:19])


@bot.message_handler(commands=['rational'])
def down(message):
    bot.send_message(message.chat.id, text='Введите число, которое хотите округлить')
    global flag
    flag = 0


@bot.message_handler(commands=['complex'])
def up(message):
    bot.send_message(message.chat.id, text='Введите числa)
    global flag
    flag = 1


@bot.message_handler(content_types=['text'])
def choise(message):
    if flag == 0:
        bot.send_message(message.chat.id, math.floor(float(message.text)))
    else:
        bot.send_message(message.chat.id, math.ceil(float(message.text)))


bot.polling(non_stop=True)
