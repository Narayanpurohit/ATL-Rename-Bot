import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26847865")
API_HASH = os.environ.get("API_HASH", "0ef9fdd3e5f1ed49d4eb918a07b8e5d6")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6757393088:AAGHQWctfdmuZt6N7GTJ9_FGqdEMNqhiK_k")

CHANNEL = os.environ.get("CHANNEL", "jn_bots") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","RENAMER_JN_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","jn_family") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","jn_bots") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","jn_dev")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Cluster0")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://jnassets75:YHoC7VLoGzvuSknay@cluster0.crje9co.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/deee1183da0b7fd7fcffe.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6789146594').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002076625671"))
