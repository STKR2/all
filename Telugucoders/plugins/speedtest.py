import asyncio
import speedtest
from pyrogram import filters
from Telugucoders import app
from config import SUDO_USERS
from Telugucoders.helpers.command import commandpro as command
from Telugucoders.helpers.filters import command, other_filters
from config import BOT_USERNAME as bname
from Telugucoders.helpers.decorators import sudo_users_only

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("- تحميل الملفات")
        test.download()
        m = m.edit("- رفع الملفات")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("انتضر قليلاً ...")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(command(["السرعة", f"سبيد"]) & ~other_filters & ~filters.edited)
async def speedtest_function(client, message):
    m = await message.reply_text("- تجربة الملفات")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**- النتيجة النهائية**
    
<u>**- العميل:**</u>
**__- الانترنت:__** {result['client']['isp']}
**__- الدولة:__** {result['client']['country']}  
<u>**- السيرفر:**</u>
**__- الإسم:__** {result['server']['name']}
**__- الدولة:__** {result['server']['country']}, {result['server']['cc']}
**__- الراعي:__** {result['server']['sponsor']}
**__- الاستجابة:__** {result['server']['latency']}  
**__- البنك:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
