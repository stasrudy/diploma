import os
from dotenv import load_dotenv, find_dotenv

#if not find_dotenv():
#    exit("Переменные окружения не загружены т.к отсутствует файл .env")
#else:
#    load_dotenv()

BOT_TOKEN = os.getenv("5935970959:AAECy_YcIq5Psi8RsiVypXQvtO4NlFU0Lys")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку")
)
