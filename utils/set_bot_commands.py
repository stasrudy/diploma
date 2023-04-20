from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS
import telebot


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )


# Создаем объект бота
bot = telebot.TeleBot("5935970959:AAECy_YcIq5Psi8RsiVypXQvtO4NlFU0Lys")

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот. Чем могу помочь?")

# Обработка команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Это список доступных команд:\n/start - начать работу с ботом\n/help - получить справку\n/echo - эхо-ответ на ваше сообщение")

# Обработка команды /echo
@bot.message_handler(commands=['echo'])
def send_echo(message):
    bot.reply_to(message, message.text)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запускаем бота
bot.polling()