from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
from _collections_abc import Mapping



updater = Updater('5509668401:AAHILPtzjfmvskjXByAO7Pf6_hEASzzyeS4')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


print('server start')
updater.start_polling()
updater.idle()