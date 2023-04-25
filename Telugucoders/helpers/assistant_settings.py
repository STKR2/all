"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


import asyncio

from config import BOT_USERNAME, SUDO_USERS

from program import LOGS
from program.utils.function import get_calls

from Telugucoders.queues import QUEUE
from Telugucoders.core import user, me_bot
from Telugucoders.filters import command, other_filters
from Telugucoders.database.dbchat import remove_served_chat
from Telugucoders.database.dbqueue import remove_active_chat
from Telugucoders.decorators import authorized_users_only, bot_creator, check_blacklist

from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired


@Client.on_message(
    command(["انضم", f"ادخل"]) & other_filters
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = (await c.get_chat(chat_id)).invite_link
        if not invitelink:
            await c.export_chat_invite_link(chat_id)
            invitelink = (await c.get_chat(chat_id)).invite_link
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await user.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ فرحان هوايه لان دزيتولي دعوة")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ موجود يمعود")


@Client.on_message(
    command(["غادر", f"userbotleave@{BOT_USERNAME}"]) & other_filters
)
@check_blacklist()
@authorized_users_only
async def leave_chat(c :Client, m: Message):
    chat_id = m.chat.id
    try:
        if chat_id in QUEUE:
            await remove_active_chat(chat_id)
            await user.leave_chat(chat_id)
            return await c.send_message(chat_id, "✅ هوه مو صوجك صوج القواد الي اجا يغنيلكم باي")
        else:
            await user.leave_chat(chat_id)
            return await c.send_message(chat_id, "✅ وانيهم طالع وياه باي")
    except UserNotParticipant:
        return await c.send_message(chat_id, "🦴 غادر منزمان لتلح")


