# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Основной скрипт бота, который отправляет сообщение в чат о количестве дней без коронавируса                       #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################

# import schedule

# from time import sleep

from tg_bot import send_alert_to_chat


# schedule.every().day.at("11:10").do(send_alert_to_chat)


if __name__ == '__main__':
    print('tg days without coronavirus counter')
    send_alert_to_chat()
