# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Модуль для получения текущей погоды в Салехарде                                                                   #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import requests


API_KEY = 'd78b8136c25cf1ece971f3c19f7f30cf'
ACCUWEATHER_API = 'Z6YbSNgBFAs3Q1oykxTPBTwvXEvkZsO8'
CITY = 'Salekhard,RU'
WEATHER_ICONS = {
    'Sunny': ''
}


def get_weather():
    req = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': CITY, 'type': 'like', 'units': 'metric', 'APPID': API_KEY})
    data = req.json()
    res = f"❄А теперь о погоде в Салехарде:\n" \
          f"🌡Температура за бортом {data['list'][0]['main']['temp']} ℃, " \
          f"☃ощущается как: {data['list'][0]['main']['feels_like']} ℃\n" \
          f"🌬Ветер: {data['list'][0]['wind']['speed']} м/с\n" \
          # f"⚗Атмосферное давление {data['list'][0]['main']['pressure']} мм.рт.ст.\n" \
          # f"💧Влажность воздуха: {data['list'][0]['main']['humidity']} %"
    return res


# def get_weather():
#     req = requests.get('http://dataservice.accuweather.com/currentconditions/v1/4660_poi',
#                        params={'apikey': ACCUWEATHER_API})
#     data = req.json()
#     res = f"❄А теперь о погоде.\nВ Салехарде сейчас:\n" \
#           f"🌡Температура за бортом {data['list'][0]['main']['temp']} ℃, " \
#           f"☃ощущается как: {data['list'][0]['main']['feels_like']} ℃\n" \
#           f"🌬Ветер: {data['list'][0]['wind']['speed']} м/с\n" \
#           f"⚗Атмосферное давление {data['list'][0]['main']['pressure']} мм.рт.ст.\n" \
#           f"💧Влажность воздуха: {data['list'][0]['main']['humidity']} %"
#     return res


if __name__ == '__main__':
    print('weather parser')
    weather = get_weather()
    print(weather)
