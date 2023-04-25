from pyrogram import Client
from config import config

__version__ = "0.6.8"

# >>> Patch = F.11.22



app = Client(
    "Telugucoders",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
) 

app.start()
