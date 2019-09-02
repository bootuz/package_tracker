import os

from telebot import TeleBot, apihelper

from helpers import parse, format_dict
from middleware import correct_message
from package import PackageData, WrongIdError

# proxies = {
#     'http': 'socks5://72.210.252.134:46164',
#     'https': 'socks5://72.210.252.134:46164'
# }
#
# apihelper.proxy = proxies
bot = TeleBot(os.environ['TOKEN'])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Пришлите индентификатор посылки")


@bot.message_handler(content_types=['text'])
def track_message(message):
    if correct_message(message.text):
        try:
            history = PackageData(message.text).history_record
            data = parse(history)
            bot.send_message(message.chat.id, format_dict(data))
        except WrongIdError:
            bot.send_message(message.chat.id, "ID не найден")
    else:
        bot.send_message(message.chat.id, 'Неверный фортмат ID')


if __name__ == '__main__':
    bot.polling(none_stop=True)
