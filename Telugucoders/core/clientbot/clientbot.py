#Telugu Coders

import os
from pyrogram import idle
from pyrogram import Client as Bot
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from pytgcalls import PyTgCalls
   
bot = Bot(
    ":telugucoders:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Telugucoders.plugins")
)

user = Client(
    STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)

call_py = PyTgCalls(user, overload_quiet_mode=True) 
with Client(":telugucoders:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
