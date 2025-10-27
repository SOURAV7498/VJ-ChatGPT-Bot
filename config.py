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

API_ID = int(environ.get("API_ID", "21140176"))
API_HASH = environ.get("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8486489329:AAEy-m491s68yi5G9asw2BzenrLhbvAZLyM")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003168773809"))
ADMINS = int(environ.get("ADMINS", "6222491731"))
DB_URI = environ.get("DB_URI", "mongodb+srv://gouravbolange_db_user:yos9d73FCsyLpiI6@cluster0.wxnzgc0.mongodb.net/?retryWrites=true&w=majority&chatgptbot=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptbot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
