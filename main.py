# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Основной скрипт бота, который отправляет сообщение в чат о количестве дней без коронавируса                       #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from datetime import datetime

from telegram import Bot
from telegram.ext import Updater
from telegram.utils.request import Request

from bot_config import API_TOKEN, CHAT_ID, ADMIN_ID


req = Request(connect_timeout=3)
bot = Bot(request=req, token=API_TOKEN)
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher


def log_error(f):
    """Отлавливание ошибок"""
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error = f'ERROR {e} in '
            print(error)
            update = args[0]
            if update and hasattr(update, 'message'):
                update.message.bot.send_message(chat_id=ADMIN_ID, text=error)
            raise e
    return inner


def count_days() -> int:
    """Считает дельту между текущим днём и стартом распространения коронавируса"""
    delta = datetime.now() - datetime(year=2019, month=12, day=1)
    res = delta.days
    return res


def get_days_word_ending(days: int) -> str:
    """Определяет окончание слова "дня", "дней" и т.д. в зависимости от входящего числа"""
    last_numeral = days % 10
    prelast_numeral = days % 100
    prelast_numeral = prelast_numeral // 10
    if prelast_numeral == 1:
        return 'дней'
    if last_numeral == 0 or last_numeral >= 5:
        return 'дней'
    elif last_numeral == 1:
        return 'день'
    else:
        return 'дня'


@log_error
def send_alert_to_chat(chat_id: int) -> None:
    """Отправляет сообщение в чат с количеством дней с момента начала распространения коронавируса"""
    days = count_days()
    bot.send_message(
        chat_id=chat_id,
        text=f'В отделе интернет проектов Ситуационного Центра ЯНАО до сих пор никто не заразился. '
             f'Прошло {days} {get_days_word_ending(days)} с момента начала распространения коронавируса.'
    )


if __name__ == '__main__':
    print('tg days without coronavirus counter')
    send_alert_to_chat(chat_id=CHAT_ID)
