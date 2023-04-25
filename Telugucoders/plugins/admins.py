#POWERED BY TELUGU CODERS

from Telugucoders.core.cache.admins import admins
from Telugucoders.core.clientbot import call_py, bot
from pyrogram import Client, filters
from Telugucoders.codersdesign.thumbnail import generate_cover
from Telugucoders.core.clientbot.queues import QUEUE, clear_queue
from Telugucoders.helpers.filters import other_filters
from Telugucoders.helpers.command import commandpro as command
from Telugucoders.helpers.decorators import authorized_users_only
from Telugucoders.core.clientbot.downloader import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP, IMG_5, NETWORK
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from Telugucoders.lang import get_command
from Telugucoders.helpers.lang import language
from Telugucoders.helpers.lang import *
from Telugucoders import app

@Client.on_message(command(["/reload", f"/reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
@language
async def update_admin(client, message, _):
    user_mention = message.from_user.mention
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(_["reload_btn"].format(user_mention)) 


@Client.on_message(command(["/skip", f"/skip@{BOT_USERNAME}", "/vskip"]) & other_filters)
@authorized_users_only
@language
async def skip(c: Client, m: Message, _):
    await m.delete()
    user_id = m.from_user.id
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await c.send_message(chat_id, _["skip_btn1"])
        elif op == 1:
            await c.send_message(chat_id, _["skip_btn2"])
        elif op == 2:
            await c.send_message(chat_id, _["skip_btn3"])
        else:
            buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text=_["close_btn"],
                            callback_data="set_close")

                ]
            ]
        )
            thumbnail = f"{IMG_5}"
            title = f"{op[0]}"
            userid = m.from_user.id
            image = await generate_cover(title, thumbnail)
            await c.send_photo(
                chat_id,
                photo=image,
                reply_markup=buttons,
                caption=_["skip_btn4"].format(m.from_user.mention) 
            ) 
    else:
        skip = m.text.split(None, 1)[1]
        OP = _["skip_btn5"], 
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["/stop", f"/stop@{BOT_USERNAME}", "/end", f"/end@{BOT_USERNAME}", "/vstop"])
    & other_filters
)
@authorized_users_only
@language
async def stop(client, m: Message, _):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply(_["stop_btn"])
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply(_["ntg_stream_btn"])


@Client.on_message(
    command(["/pause", f"/pause@{BOT_USERNAME}", "/vpause"]) & other_filters
)
@authorized_users_only
@language
async def pause(client, m: Message, _):
    user_mention = m.from_user.mention
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(_["pause_btn"].format(user_mention)) 
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply(_["ntg_stream_btn"])


@Client.on_message(
    command(["/resume", f"/resume@{BOT_USERNAME}", "/vresume"]) & other_filters
)
@authorized_users_only
@language
async def resume(client, m: Message, _):
    user_mention = m.from_user.mention
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(_["resume_btn"].format(user_mention))
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply(_["ntg_stream_btn"])
