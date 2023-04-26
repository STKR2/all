import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from Telugucoders.helpers.filters import command
from Telugucoders.helpers.filters import command, other_filters
from Telugucoders.helpers.command import commandpro as command
from Telugucoders.helpers.decorators import sudo_users_only
from Telugucoders.core.database.dbchat import get_served_chats
from Telugucoders.core.database.dbpunish import add_gban_user, is_gbanned_user, remove_gban_user
from Telugucoders.helpers.lang import language
from Telugucoders.helpers.lang import *

from Telugucoders.plugins.language import keyboard
from Telugucoders.lang import get_command
from Telugucoders.helpers.lang import languageCB
from config.config import BOT_NAME, SUDO_USERS, BOT_USERNAME as bn


@Client.on_message(command(["عام", f"gban@{bn}"]) & ~filters.edited)
@sudo_users_only
@language
async def global_banned(c: Client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text(_["gban_1"])
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await c.get_users(user)
        from_user = message.from_user
        BOT_ID = await c.get_me()
        if user.id == from_user.id:
            return await message.reply_text(
                "You can't gban yourself !"
            )
        elif user.id == BOT_ID:
            await message.reply_text(_["gban_2"])
        elif user.id in SUDO_USERS:
            await message.reply_text(_["gban_3"])
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(_["gban_4"].format(user.mention, len, served_chats)
            )
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.ban_chat_member(num, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
 **- تم حظر عام نهائيا من [{BOT_NAME}](https://t.me/{bn})

**- الرسالة:** {message.chat.title} [`{message.chat.id}`]
**- اسم المطور:** {from_user.mention}
**- يوزر المحظور:** {user.mention}
**- ايدي المستخدم:** `{user.id}`
**- المجموعة:** `{number_of_chats}`"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    BOT_ID = await c.get_me()
    if user_id == from_user_id:
        await message.reply_text(_["gban_14"])
    elif user_id == BOT_ID:
        await message.reply_text(_["gban_2"])
    elif user_id in SUDO_USERS:
        await message.reply_text(_["gban_3"])
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text(_["gban_15"])
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(_["gban_4"].format(mention, len, served_chats)
            )
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.ban_chat_member(num, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
 **- تم حظر عام نهائي من [{BOT_NAME}](https://t.me/{bn})

**- الرسالة:** {message.chat.title} [`{message.chat.id}`]
**- يوزر المطور:** {from_user_mention}
**- يوزر المحظور:** {mention}
**- الايدي:** `{user_id}`
**- المجموعة:** `{number_of_chats}`"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@Client.on_message(command(["الغاء", f"ungban@{bn}"]) & ~other_filters & ~filters.edited)
@sudo_users_only
@language
async def ungban_global(c: Client, message: Message, _):
    chat_id = message.chat.id
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(_["gban_5"]
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await c.get_users(user)
        from_user = message.from_user
        BOT_ID = await c.get_me()
        if user.id == from_user.id:
            await message.reply_text(_["gban_6"])
        elif user.id == BOT_ID:
            await message.reply_text(_["gban_7"])
        elif user.id in SUDO_USERS:
            await message.reply_text(_["gban_8"])
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text(_["gban_9"])
            else:
                await c.unban_chat_member(chat_id, user.id)
                await remove_gban_user(user.id)
                await message.reply_text(_["gban_10"])
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    BOT_ID = await c.get_me()
    if user_id == from_user_id:
        await message.reply_text(_["gban_11"])
    elif user_id == BOT_ID:
        await message.reply_text(_["gban_11"])
    elif user_id in SUDO_USERS:
        await message.reply_text(_["gban_12"])
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text(_["gban_6"])
        else:
            await c.unban_chat_member(chat_id, user_id)
            await remove_gban_user(user_id)
            await message.reply_text(_["gban_14"])
