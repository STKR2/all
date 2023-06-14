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

API_ID = int(getenv("API_ID", "28817643"))
API_HASH = getenv("API_HASH", "d3af44df9cfcbd0da97a23cbf7307123")
BOT_TOKEN = getenv("BOT_TOKEN", "6126802144:AAGl8jgfOj1xUk35LP0XHyXbo_oAM4_qCoE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BACKgWwqiSkR3F6KFnAtpsNycnENuNDi4SOTr16jXzLL31JikX6IzsFOac0JIQXxApFg-L4rXOzyC_vw-Z9aklaBrf653qB9VcyWL-xXDyoDsT0fvgY9li0z4XPWRZ4gn6VfcPPhjCQ7T1Xd2UwK4xzlPqOl2FFuku-f95c5jjMddlHPpqWub2IMe1XTd3O7LU6R36raG6A5bSb_YXQRl3NDGhkt-zcUuD2EUY2QJjy7IVAhVQcCdW1I97RgnvGxcWnh2bPmGn-8ahN7OJpm1pg6Q88jnR7tKvGRw9NaoQeltyUlOOsQiIUgamojA1lDGBzU26CPp6PYzfiX0iXq0c3JAAAAAXXvvNAA")
BOT_USERNAME = getenv("BOT_USERNAME", "fer3oonmusicbot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6273613008").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6273613008").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "xl444")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


