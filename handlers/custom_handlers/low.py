from telebot.types import Message
from loader import bot
from config_data.config import RAPID_API_KEY
import requests
import json
import pprint

@bot.message_handler(commands=["low"])
def bot_low(message: Message):
    location = input('В каком городе ищем отель?')
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"
    querystring = {"query": location, "locale": "ru_RU", "currency": "USD"}

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    pprint.pprint(response.json())


#DEFAULT_COMMANDS = (
#    ("start", "Запустить бота"),
#    ("help", "Вывести справку"),
#    ("echo", "Повторить сообщение"),
#    ('low', 'Поиск низких цен')
#)

#bot.set_my_commands(
#        [BotCommand(*i) for i in DEFAULT_COMMANDS]


#спросить какой город
#дать выбрать варианты городов вытянутые из API - обращение к API
#получить по выбранному варианту ID локации
#по этому ID найти с самой низкой ценой hotel - обращение к API

