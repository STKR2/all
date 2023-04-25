# ©Telugu Coders music projects
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from Telugucoders.codersdesign.thumbnail import generate_cover
from Telugucoders.helpers.filters import command, other_filters
from Telugucoders.core.clientbot.queues import QUEUE, add_to_queue
from Telugucoders.core.clientbot import call_py, user
from Telugucoders.core.clientbot.downloader import bash
from Telugucoders.helpers.gets import get_url, get_file_name
from config import BOT_USERNAME, IMG_5, DURATION_LIMIT, GROUP, NETWORK
from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch
from Telugucoders.helpers.lang import language
from Telugucoders.helpers.lang import *
from Telugucoders.plugins.language import keyboard
from Telugucoders.lang import get_command
from Telugucoders.helpers.lang import languageCB

def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


# async def ytdl(format: str, link: str):
#    stdout, stderr = await bash(f'yt-dlp --geo-bypass -g -f "[height<=?720][width<=?1280]" {link}')
#    if stdout:
#        return 1, stdout.split("\n")[0]
#    return 0, stderr

async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()

#plus
useer = "NaN"

@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@language
async def play(c: Client, m: Message, _):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    if m.sender_chat:
        return await m.reply_text(_["music_1"])
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(_["music_2"])
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(_["music_3"])
        return
    if not a.can_delete_messages:
        await m.reply_text(_["music_4"])
        return
    if not a.can_invite_users:
        await m.reply_text(_["music_5"])
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await c.unban_chat_member(chat_id, ubot)
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
    except UserNotParticipant:
        try:
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            return await m.reply_text(_["music_7"].format(e))
    if replied:
        if replied.audio or replied.voice:
            Telugu = await replied.reply(_["music_8"])
            dl = await replied.download()
            link = replied.link
            
            try:
                if replied.audio:
                    songname = replied.audio.title[:70]
                    songname = replied.audio.file_name[:70]
                    duration = replied.audio.duration
                elif replied.voice:
                    songname = "Voice Note"
                    duration = replied.voice.duration
            except BaseException:
                songname = "Audio"
    
    await m.delete()
    audio = (
        (m.reply_to_message.audio or m.reply_to_message.voice)
        if m.reply_to_message
        else None
    )
    url = get_url(m) 

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(_["music_9"].format(DURATION_LIMIT))
   
            if chat_id in QUEUE:
                title = songname
                userid = m.from_user.id
                requested_by = m.from_user.first_name
                duration = round(audio.duration / 60)
                views = "Locally added"
                thumbnail = f"{IMG_5}"
                image = await generate_cover(requested_by, title, views, duration, thumbnail)
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(_["vid_btn"], callback_data="menu"), 
                        InlineKeyboardButton(_["close_btn"], callback_data="set_close")
                ]
            ]
        )
                await Telugu.delete()
                await m.reply_photo(
                    photo="final.png",
                    reply_markup=buttons,
                    caption=_["music_10"].format(pos),
                )
            else:
                try:
                    title = songname
                    userid = m.from_user.id
                    requested_by = m.from_user.first_name
                    duration = round(audio.duration / 60)
                    views = "Locally added"
                    thumbnail = f"{IMG_5}"
                    image = await generate_cover(requested_by, title, views, duration, thumbnail)
                    await Telugu.edit(_["music_11"])
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                            HighQualityAudio(),
                        ),
                        stream_type=StreamType().local_stream,
                    )
                    add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                    await Telugu.delete()
                    buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(_["vid_btn"], callback_data="menu"), 
                        InlineKeyboardButton(_["close_btn"], callback_data="set_close")
                ]
            ]
        )
                    await m.reply_photo(
                        photo="final.png",
                        reply_markup=buttons,
                        caption=_["music_12"],
                    )
                except Exception as e:
                    await Telugu.delete()
                    await m.reply_text(f"🚫 ᴇʀʀᴏʀ:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(_["music_13"]) 
            else:
                Telugu = await c.send_message(chat_id, "🔍")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await Telugu.edit(_["music_14"])
                else:
                    results = YoutubeSearch(url, max_results=1).to_dict()
                    # print results
                    songname = search[0]
                    title = results[0]["title"]
                    url = results[0]["url"]
                    requested_by = m.from_user.first_name
                    duration = results[0]["duration"]
                    views = results[0]["views"]
                    thumbnail = results[0]["thumbnails"][0]
                    userid = m.from_user.id
                    image = await generate_cover(requested_by, title, views, duration, thumbnail)
                    coders, ytlink = await ytdl(url)
                    if coders == 0:
                        await Telugu.edit(_["music_15"].format(ytlink))
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await Telugu.delete()
                            buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(_["vid_btn"], callback_data="menu"), 
                        InlineKeyboardButton(_["close_btn"], callback_data="set_close")
                ]
            ]
        )
                            await m.reply_photo(
                                photo="final.png",
                                reply_markup=buttons,
                                caption=_["music_16"].format(pos))
                        else:
                            try:
                                await Telugu.edit(_["music_17"])
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await Telugu.delete()
                                buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(_["vid_btn"], callback_data="menu"), 
                        InlineKeyboardButton(_["close_btn"], callback_data="set_close")
                ]
            ]
        )
                                await m.reply_photo(
                                    photo="final.png",
                                    reply_markup=buttons,
                                    caption=_["music_12"].format(requested_by))
                            except Exception as ep:
                                await Telugu.delete()
                                await m.reply_text(f"🚫 ᴇʀʀᴏʀ: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(_["music_13"])
        else:
            Telugu = await c.send_message(chat_id, "🔍")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await Telugu.edit(_["music_14"])
            else:
                results = YoutubeSearch(query, max_results=5).to_dict()
                songname = search[0]
                title = results[0]["title"]
                url = search[1]
                requested_by = m.from_user.first_name
                duration = results[0]["duration"]
                views = results[0]["views"]
                thumbnail = results[0]["thumbnails"][0]
                userid = m.from_user.id
                image = await generate_cover(requested_by, title, views, duration, thumbnail)
                coders, ytlink = await ytdl(url)
                if coders == 0:
                    await Telugu.edit(_["music_15"].format(ytlink))
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await Telugu.delete()
                        buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(_["vid_btn"], callback_data="menu"), 
                        InlineKeyboardButton(_["close_btn"], callback_data="set_close")
                ]
            ]
        )
                        await m.reply_photo(
                            photo="final.png",
                            reply_markup=buttons,
                            caption=_["music_10"].format(pos))
                    else:
                        try:
                            await Telugu.edit(_["music_11"])
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await Telugu.delete()
                            buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(_["vid_btn"], callback_data="menu"), 
                        InlineKeyboardButton(_["close_btn"], callback_data="set_close")
                ]
            ]
        )
                            await m.reply_photo(
                                photo="final.png",
                                reply_markup=buttons,
                                caption=_["music_12"].format(m.chat.title, m.chat.id, requested_by))
                        except Exception as ep:
                            await Telugu.delete()
                            await m.reply_text(f"🚫 ᴇʀʀᴏʀ: `{ep}`")

                        try:
                            os.remove("final.png")
                        except Exception:
                            pass
                        return

