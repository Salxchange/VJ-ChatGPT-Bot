import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "23941369"))
API_HASH = environ.get("API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd")
BOT_TOKEN = environ.get("BOT_TOKEN", "6609713747:AAH7Ijmim8l-dzaw2fn_0eB8aZgikanVVzc")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002093365834"))
ADMINS = int(environ.get("ADMINS", "6805306768"))
DB_URI = environ.get("DB_URI", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
