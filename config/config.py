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

#------------------------ Important Stuff 😌 -----------------------

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION")
BOT_USERNAME = getenv("BOT_USERNAME", "Amalamusic_bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6168241978").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5566634044").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001792664572")) 

MONGODB_URL = getenv("MONGODB_URL")
#________________________ Updates 🍃 & Music bot name________________
NETWORK = getenv("NETWORK", "Telugucodersupdates")
GROUP = getenv("GROUP", "tgshadow_fighters")
BOT_NAME = getenv("BOT_NAME", "Amala Music")
BANNED_USERS = filters.user()

#************************* Image Stuff 💕 ****************************

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg")

aiohttpsession = aiohttp.ClientSession()


