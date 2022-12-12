from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    help_msg = '''
                /hi - поздароваться
                /time - показать текущее время 
                /help - отобразить эту справку с командами
                /sum x y - получение суммы целых чисел, которые надо вписать на места x и y
                /sub x y - получение разности целых чисел, которые надо вписать на места x и y
                /mult x y - получение произведения целых чисел, которые надо вписать на места x и y
                /mult x y - получение чатного от деления, целых чисел, которые надо вписать на места x и y
                /csum x y - получение суммы комплексных чисел, которые надо вписать на места x и y
                /csub x y - получение разности комплексных чисел, которые надо вписать на места x и y
                /cmult x y - получение произведения комплексных чисел, которые надо вписать на места x и y
                /cdiv x y - получение чатного от деления, комплексных чисел, которые надо вписать на места x и y
                '''
    update.message.reply_text(help_msg)

#  /time


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

# /sum 12 25


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # '/sum', '12+3j', '25'
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')


def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')


def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} / {y} = {x / y}')


# /csum 12 25
def csum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # '/sum', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def csub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')


def cmult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')


def cdiv_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} / {y} = {x / y}')
