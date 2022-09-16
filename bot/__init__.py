from os import getenv, mkdir

from dotenv import load_dotenv
from pyrogram.client import Client

load_dotenv()

ADMINS = getenv('ADMINS', '').split()
BASE_FOLDER = getenv('DOWNLOAD_FOLDER', '/data')
DL_FOLDER = BASE_FOLDER

try:
    mkdir(DL_FOLDER)
except FileExistsError:
    pass

app = Client(
    name=__name__,
    api_id=int(getenv('TELEGRAM_API_ID')),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('BOT_TOKEN')
)
