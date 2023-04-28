## ©copyright infringement on Telugu Coders

import asyncio
from time import time
from datetime import datetime
from Telugucoders.helpers.filters import command, other_filters
from Telugucoders.helpers.command import commandpro as command
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import GROUP, NETWORK, BOT_USERNAME, OWNER_ID, BOT_NAME, BANNED_USERS
from pytgcalls import (__version__ as pytover)
from Telugucoders import __version__
from sys import version_info
from Telugucoders.core.database.dbchat import add_served_chat, is_served_chat
from Telugucoders.core.database.dblockchat import blacklisted_chats
from Telugucoders.core.clientbot.clientbot import me_bot
from Telugucoders.lang import get_command
from Telugucoders.helpers.lang import language
from Telugucoders.helpers.lang import *
from Telugucoders import app
__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

    
   ## don't change any value in this repo if you change the value bot will crash your heroku accounts. 

@Client.on_message(command("/start") & ~filters.edited & ~BANNED_USERS)
@language
async def start_(client: Client, message: Message, _):
    user_mention = message.from_user.mention
    start_keyboard = InlineKeyboardMarkup( [[
           InlineKeyboardButton(_["help_btn"], callback_data="command_list"), 
           ],[
           InlineKeyboardButton(_["support_btn"], url=f"https://t.me/{GROUP}"),  
           ],[
           InlineKeyboardButton(_["owner_btn"], url=f"tg://settings"),  

           ]]
           )
    chat_id = message.chat.id
    if chat_id > 0:
        mention = message.from_user.mention 
        await message.reply_text(_["start1"].format(user_mention),reply_markup=start_keyboard) 
    else:
        await message.reply_text("- موجود موجود لتخاف")
         
@Client.on_message(command("النشاط") & filters.group & ~filters.edited & ~BANNED_USERS)
@language
async def alive(client: Client, message: Message, _):    
    user_mention = message.from_user.mention
    alive_keyboard = InlineKeyboardMarkup( [[
           InlineKeyboardButton(_["close_btn"], callback_data="set_close")
           ]]
           ) 
    await message.reply_text(_["alive_start"].format(user_mention),reply_markup=alive_keyboard)

@Client.on_message(command(["السورس", "سورس"]) & filters.group & ~filters.edited)
@language
async def repo(client: Client, message: Message, _):
    source_keyboard = InlineKeyboardMarkup( [[
           InlineKeyboardButton(_["source"], url="https://t.me/Xl444")
           ]]
           ) 
    await message.reply_text(_["repo_btn"],reply_markup=source_keyboard) 

@Client.on_message(command("مساعدة") & filters.private & ~other_filters & ~filters.edited & ~BANNED_USERS) 
@language
async def help(client: Client, message: Message, _):
    help_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["owner_cmds"], callback_data="owner_command"), 
          ],[
          InlineKeyboardButton(_["sudo_user"], callback_data="sudo_command"), 
          InlineKeyboardButton(_["user_cmds"], callback_data="user_commands"), 
          ],[
          InlineKeyboardButton(_["back_home"], callback_data="home_start"),
          ]]
          ) 
    await message.reply_text(_["help_button"],reply_markup=help_keyboard) 


@Client.on_message(command("الاوامر") & filters.group & ~filters.edited) 
@language
async def ghelp(client: Client, message: Message, _):
    ghelp_keyboard = InlineKeyboardMarkup( [[
           InlineKeyboardButton(_["ghelp_btn"], callback_data="user_commands")
           ]]
           ) 
    await message.reply_text(_["ghelp_text"],reply_markup=ghelp_keyboard) 
        
@Client.on_message(command("المطور") & filters.group & ~filters.edited & ~BANNED_USERS)
@language
async def get_uptime(c: Client, message: Message, _):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    user_mention = message.from_user.mention
    uptime_keyboard = InlineKeyboardMarkup( [[
           InlineKeyboardButton(_["close_btn"], callback_data="set_close")
           ]]
           ) 
    await message.reply_text(_["uptime_btn"].format(uptime,user_mention,START_TIME_ISO),reply_markup=uptime_keyboard) 

                 
@Client.on_message(command("بنك") & filters.group & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("**جاري حساب البنك ..**")
    delta_ping = time() - start
    await m_reply.edit_text(" **- بنك البوت!**\n" f" **{delta_ping * 1000:.3f} مللي ثانية**")
