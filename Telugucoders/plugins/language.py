from Telugucoders.lang import get_string
from Telugucoders.core.database.language import set_lang, get_lang
from Telugucoders import app
from config import LOG_GROUP_ID
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message
from Telugucoders.helpers.lang import language


keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="🇱🇷 English", callback_data="languages_en")],
     [InlineKeyboardButton(text="🇮🇳 हिन्दी", callback_data="languages_hi"),
      InlineKeyboardButton(text="🇮🇳 తెలుగు", callback_data="languages_te")], 
     [InlineKeyboardButton(text="🇮🇳 Malayalam", callback_data="languages_ml"),
      InlineKeyboardButton(text="🇷🇺 Russia", callback_data="languages_ru")], 
     [InlineKeyboardButton(text="✘ Back", callback_data="home_start")]])

grp_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="🇱🇷 English", callback_data="languages_en")],
     [InlineKeyboardButton(text="🇮🇳 हिन्दी", callback_data="languages_hi"),
      InlineKeyboardButton(text="🇮🇳 తెలుగు", callback_data="languages_te")], 
     [InlineKeyboardButton(text="🇮🇳 Malayalam", callback_data="languages_ml"),
      InlineKeyboardButton(text="🇷🇺 Russia", callback_data="languages_ru")], 
     [InlineKeyboardButton(text="🗑 Bin", callback_data="set_close")]])

@app.on_message(filters.command("lang"))
@language
async def langs_command(client, message: Message, _):
    userid = message.from_user.id if message.from_user else None
    chat_type = message.chat.type
    if chat_type == "private":await message.reply_text("Choose Your languages",reply_markup=keyboard)
    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id
        st = await app.get_chat_member(group_id, userid)
        if(st.status != "administrator" and st.status != "creator"):
         return 
        try:   
         await message.reply_text( "Choose Your languages",reply_markup=grp_keyboard)
        except Exception as e:
         return await app.send_message(LOG_GROUP_ID,text= e)


@app.on_callback_query(filters.regex("languages"))
async def language_markup(_, CallbackQuery):
    langauge = (CallbackQuery.data).split("_")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
      return await CallbackQuery.answer("You're already on same language")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer("✅ Successfully changed your language.", show_alert=True)
    except:
        return await CallbackQuery.answer(
            "This language is Under Construction 👷", show_alert=True)
    await set_lang(CallbackQuery.message.chat.id, langauge)
    return await CallbackQuery.edit_message_reply_markup(f"{CallbackQuery.message.from_user.mention} Was Successfully changed My language ✅\n From {old} to {langauge},reply_markup=keyboard")
