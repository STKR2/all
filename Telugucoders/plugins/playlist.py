from config.config import SERVER_PLAYLIST_LIMIT, BANNED_USERS
from Telugucoders.core.carbon.carbon import Carbon
from Telugucoders.core.YouTube.youtube import Youtube
from Telugucoders.helpers.lang import languageCB
from Telugucoders.helpers.lang import *
from Telugucoders.helpers.lang import language
from Telugucoders.plugins.language import keyboard
from Telugucoders.lang import get_command
from Telugucoders import app
import os
from random import randint
from Telugucoders.core.database.playlistdb import delete_playlist, get_playlist, get_playlist_names, save_playlist
import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pykeyboard import InlineKeyboard


BASE = "https://batbin.me/"

async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data

async def TC_CODERS(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link
  

@app.on_message(filters.command("playlist") & ~filters.edited & ~BANNED_USERS)
@language
async def check_playlist(client, message: Message, _):
    _playlist = await get_playlist_names(message.from_user.id)
    if _playlist:
        get = await message.reply_text(_["playlist1"])
    else:
        return await message.reply_text(_["playlist2"])
    msg = _["playlist_3"]
    count = 0
    for telugucoders in _playlist:
        _note = await get_playlist(message.from_user.id, shikhar)
        title = _note["title"]
        title = title.title()
        duration = _note["duration"]
        count += 1
        msg += f"\n\n{count}- {title[:70]}\n"
        msg += _["playlist4"].format(duration)
    link = await TC_CODERS(msg)
    lines = msg.count("\n")
    if lines >= 17:
        car = os.linesep.join(msg.split(os.linesep)[:17])
    else:
        car = msg
    carbon = await Carbon.generate(car, randint(100, 10000000000))
    await get.delete()
    await message.reply_photo(
        carbon, caption=_["playlist5"].format(link)
    )
    
@app.on_callback_query(filters.regex("add_playlist") & ~BANNED_USERS)
@languageCB
async def add_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
    if await get_playlist(user_id, videoid):
        try:
            return await CallbackQuery.answer(_["playlist6"], show_alert=True)
        except:
            return
    if len(await get_playlist_names(user_id)) == SERVER_PLAYLIST_LIMIT:
        try:
            return await CallbackQuery.answer(_["playlist7"].format(SERVER_PLAYLIST_LIMIT), show_alert=True)
        except:
            return
    title, duration_min, duration_sec, thumbnail, vidid, link = await Youtube.details(videoid, True)
    title = title.title()[:50]
    plist = {
        "videoid": vidid,
        "title": title,
        "duration": duration_min,
    }
    await save_playlist(user_id, videoid, plist)
    try:
        return await CallbackQuery.answer(_["playlist8"].format(title), show_alert=True)
    except:
        return

@app.on_callback_query(filters.regex("del_playlist") & ~BANNED_USERS)
@languageCB
async def del_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
    deleted = await delete_playlist(user_id, videoid)
    if deleted:
        try:
            await CallbackQuery.answer(_["playlist9"], show_alert=True)
        except:
            pass
    else:
        try:
            return await CallbackQuery.answer(_["playlist10"], show_alert=True)
        except:
            return 
