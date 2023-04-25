## ©copyright infringement on Telugu Coders

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters          
import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from Telugucoders.core.clientbot import clientbot
from Telugucoders.core.clientbot.clientbot import me_bot
from config import GROUP, NETWORK, BOT_USERNAME, SUDO_USERS, OWNER_ID, IMG_5, MONGODB_URL
from Telugucoders.helpers.lang import languageCB
from Telugucoders import app
from Telugucoders.helpers.decorators import authorized_users_only
from Telugucoders.helpers.lang import *
from Telugucoders.plugins.language import keyboard
from Telugucoders.lang import get_command
from Telugucoders.core.clientbot.queues import QUEUE, clear_queue
from Telugucoders.core.clientbot import call_py
from Telugucoders.core.clientbot.downloader import skip_current_song, skip_item
from Telugucoders.core.YouTube.youtube import Youtube

## don't change any value in this repo if you change the value bot will crash your heroku accounts. 


@Client.on_callback_query(filters.regex("home_start"))
@languageCB
async def home_start(client, CallbackQuery, _):
    user_mention = CallbackQuery.from_user.mention
    start_keyboard = InlineKeyboardMarkup( [[
           InlineKeyboardButton(_["help_btn"], callback_data="command_list"), 
           ],[
           InlineKeyboardButton(_["support_btn"], url=f"https://t.me/{GROUP}"), 
           InlineKeyboardButton(_["network_btn"], url=f"https://t.me/{NETWORK}"), 
           ],[
           InlineKeyboardButton(_["git_repo"], url="https://github.com/TeluguCodersMusic/Amalav2.0"), 
           InlineKeyboardButton(_["owner_btn"], url=f"t.me/santhu_afk_bot7981"), 
           ],[
           InlineKeyboardButton(_["lang_btn"], callback_data="_langs")
           ]]
           )  
    await CallbackQuery.edit_message_text(_["start1"].format(user_mention),reply_markup=start_keyboard)       
   
@Client.on_callback_query(filters.regex("command_list"))
@languageCB
async def commands_set(client, CallbackQuery, _):
    help_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["owner_cmds"], callback_data="owner_command"), 
          ],[
          InlineKeyboardButton(_["sudo_user"], callback_data="sudo_command"), 
          InlineKeyboardButton(_["user_cmds"], callback_data="user_commands"), 
          ],[
          InlineKeyboardButton(_["support_btn"], url=f"https://t.me/{GROUP}"), 
          InlineKeyboardButton(_["network_btn"], url=f"https://t.me/{NETWORK}"),  
          ],[
          InlineKeyboardButton(_["back_home"], callback_data="home_start"),
          InlineKeyboardButton(_["close_btn"], callback_data="close_panel") 
          ]]
          )  
    await CallbackQuery.edit_message_text(_["help_button"],reply_markup=help_keyboard) 

@Client.on_callback_query(filters.regex("sudo_command"))
@languageCB
async def sudo_set(client, CallbackQuery, _):
    user_id = CallbackQuery.from_user.id
    BOT_NAME = me_bot.first_name
    sudo_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["back_home"], callback_data="command_list"), 
          ]]
          ) 
    if user_id not in SUDO_USERS:
        await CallbackQuery.answer(_["alert_btn"], show_alert=True)
        return
    await CallbackQuery.edit_message_text(_["sudo_cmds"].format(BOT_NAME),reply_markup=sudo_keyboard) 
        
@Client.on_callback_query(filters.regex("owner_command"))
@languageCB
async def owner_set(client, CallbackQuery, _):
    user_id = CallbackQuery.from_user.id
    BOT_NAME = me_bot.first_name
    owner_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["back_home"], callback_data="command_list"), 
          ]]
          ) 
    if user_id not in OWNER_ID:
        await CallbackQuery.answer(_["alert_btn1"], show_alert=True)
        return
    await CallbackQuery.edit_message_text(_["owner_cmds2"].format(BOT_NAME),reply_markup=owner_keyboard) 

@Client.on_callback_query(filters.regex("user_commands"))
@languageCB
async def user_commands(client, CallbackQuery, _):
    BOT_NAME = me_bot.first_name
    users_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["back_home"], callback_data="command_list"), 
          ]]
          ) 
    await CallbackQuery.edit_message_text(_["user_cmds2"].format(BOT_NAME),reply_markup=users_keyboard) 
        
   
@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🚨 You don't have access to perform this action\n\n👨‍💼Only Admin Can Manage This Button\n\nIf you Believe your the Admin please /reload Bot", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(
        text = "Choose Your languages:", 
        reply_markup = keyboard,
        disable_web_page_preview=True)

@Client.on_callback_query(filters.regex("end"))
@languageCB
async def end(client: Client, query: CallbackQuery, _):
    data = query.data
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.message.reply_text(_["stop_btn"])
        except Exception as e:
            await query.message.reply_text(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await query.message.reply_text(_["ntg_stream_btn"])

@Client.on_callback_query(filters.regex("^pause$"))
@languageCB
async def pause(client, query: CallbackQuery, _):
    user_mention = query.from_user.mention
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
        except Exception as e:
            await query.answer(text=f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
        await query.message.reply_text(_["pause_btn"].format(user_mention))
    else:
        await query.message.reply_text(_["ntg_stream_btn"])

@Client.on_callback_query(filters.regex("^resume$"))
@languageCB
async def resume(client: Client, query: CallbackQuery, _):
    chat_id = query.message.chat.id
    user_mention = query.from_user.mention
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.message.reply_text(_["resume_btn"].format(user_mention))
        except Exception as e:
            await query.answer(f"Error resuming stream: {e}")
    else:
        await query.message.reply_text(_["ntg_stream_btn"])
        
@Client.on_callback_query(filters.regex("^skip$"))#
@languageCB
async def skip(client: Client, callback_query: CallbackQuery, _):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    data = callback_query.data

    if data == "skip":
        await client.answer_callback_query(callback_query.id)

        op = await skip_current_song(chat_id)
        if op == 0:
            await callback_query.message.edit_text(_["skip_btn1"])
        elif op == 1:
            await callback_query.message.edit_text(_["skip_btn2"])
        elif op == 2:
            await callback_query.message.edit_text(_["skip_btn3"])
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
            duration = 0  # Set duration to some value
            image = await generate_cover(title, duration, thumbnail)
            await callback_query.message.edit_photo(
                photo=image,
                reply_markup=buttons,
                caption=_["skip_btn4"].format(callback_query.from_user.mention)
            )
    else:
        skip = data.split("_", 1)[1]
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
            await callback_query.message.reply_text(OP)
            

@Client.on_callback_query(filters.regex("global_calls"))
@languageCB
async def global_calls(client, CallbackQuery, _):
    calls_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["group_calls"], callback_data="group_calls"), 
          InlineKeyboardButton(_["personal_calls"], callback_data="personal_calls"), 
          ],[
          InlineKeyboardButton(_["back_home"], callback_data="menu")
          ]]
          ) 
    await CallbackQuery.answer("Powered by: Telugu coders\n\nGetting your calls...", show_alert=True) 
    await CallbackQuery.message.reply_text(_["calls_text"], reply_markup=calls_keyboard) 
    
@Client.on_callback_query(filters.regex("playlist"))
@languageCB
async def playlist(client, CallbackQuery, _):
    data = CallbackQuery.data
    if data.startswith("playlist"):
        videoid = data.split(None, 1)[1]
        await Youtube.details(videoid, True)
        chat_id = CallbackQuery.message.chat.id
        play_keyboard = InlineKeyboardMarkup( [[
              InlineKeyboardButton(_["playlist_btn1"], callback_data=f"add_playlist {video_id}"), 
              InlineKeyboardButton(_["playlist_btn2"], callback_data="del_playlist"), 
              ],[
              InlineKeyboardButton(_["back_home"], callback_data="menu")
              ]]
              ) 
        await CallbackQuery.answer("Powered by: Telugu coders\n\nGetting your Playlist...", show_alert=True) 
        await CallbackQuery.message.reply_text(_["playlist_text"], reply_markup=play_keyboard)
    
@Client.on_callback_query(filters.regex("menu"))
@languageCB
async def menu(client, CallbackQuery, _):
    a = await app.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.can_manage_voice_chats:
        return await CallbackQuery.answer("🚨 You don't have access to perform this action\n\n👨‍💼Only Admin Can Manage This Button\n\nIf you Believe your the Admin please /reload Bot", show_alert=True)
    menu_keyboard = InlineKeyboardMarkup( [[
          InlineKeyboardButton(_["skip"], callback_data="skip"), 
          InlineKeyboardButton(_["resume"], callback_data="resume"), 
          InlineKeyboardButton(_["pause"], callback_data="pause"), 
          InlineKeyboardButton(_["end"], callback_data="end"), 
          ],[
          InlineKeyboardButton(_["playlist"], callback_data="playlist"),
          InlineKeyboardButton(_["Global_calls"], callback_data="global_calls"), 
          ],[
          InlineKeyboardButton(_["close_btn"], callback_data="close_panel")
          ]]
          )  
    await CallbackQuery.edit_message_text(_["menu_button"],reply_markup=menu_keyboard) 
