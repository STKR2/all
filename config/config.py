import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "25711100"))
API_HASH = getenv("API_HASH", "0118cc1662da972d0206420a7886769a")
BOT_TOKEN = getenv("BOT_TOKEN", "6034374468:AAEnB8MuEres4zWPFWWrB898n3YNGN-lqq0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BACDtgfAbRPySB7Ab1IEp9SZsAHR6op-_vB_72_X3ZMEKZHQnY5WJk-sj86O9rT9cyBXY_WwyUaclQ0OI3vaW-l_TguqQ7GA0N7YkYbTB1OUgDu3fcUNS9VDG2Aa8knARAhhuZBZ6kdaXCHxQzBvNhML4HTfMAxo2yxbJlqiMLUYTa93n_6h-5fp-QsZ-ZFnWZ2mvd6Xuj9-K5btKA09AjrbU1gy3eqZM5qohrOyb-cK3-aQwi-2NKvuzl5-Rc83oypKdclAPPs4WbLlW0r4icauhi9IyS70oFCpepA3mU6uJkmBusQ5xQfqprYEPbIXrSvy95gK-sjA2-yFVNLwAo67ULf5dwA")
BOT_USERNAME = getenv("BOT_USERNAME", "B78_Bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1354234231").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1354234231").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "DAD_MIDO")
GROUP = getenv("GROUP", "DAD_MIDO")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


