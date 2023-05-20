from telebot.types import Message
from loader import bot
import requests
import json


@bot.message_handler(commands=["low"])
def bot_low(message: Message):
    my_request = requests.get('https://rapidapi.com/apidojo/api/hotels4/properties/v2/list')
    data = json.loads(my_request.text)
    print(data)



