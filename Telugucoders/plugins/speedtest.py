import asyncio
import speedtest
from pyrogram import filters
from Telugucoders import app
from config import SUDO_USERS
from Telugucoders.helpers.filters import command, other_filters
from config import BOT_USERNAME as bname
from Telugucoders.helpers.decorators import sudo_users_only

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ")
        test.download()
        m = m.edit("ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(command(["speedtest", f"speedtest@{bname}"]) & ~filters.edited)
@sudo_users_only
async def speedtest_function(client, message):
    m = await message.reply_text("ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅ ᴛᴇsᴛ")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**Client:**</u>
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
<u>**Server:**</u>
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
