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

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "6394890638:AAHvh2Z7XtAtTMsNvPoQgMuM9BIPtIXkWKY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BAC2TzI1e7RICVUeT0pAQVjDHfNf7ZeahLnBNgMYXQABCXRmaay_kKwgZBIim5rBxOlLnVhriuMpwutDAXXaPKrnlXnW1RN23LfKPSf52GYPPNRYMrh9uQq1z8fF06nirQ-CcnjqDE2uP-I1eXtbmTFLwH5mMguxwOsiJJ4czd4L4LQXbF4fSk39efSxL_is_Kqx3CxM6qOhd78mdIH82kcXdoKWCv1TnmLJb_KenWG20D80i5JWnDJvozXT5Ml0o_-w1aknE9zS8IoCsMt-evhgW6e6lrEc8e8INq_MCGdW1Hzbc2sG-J1GgFeBFsM8C8Jtc22Vcg5BevUuW-BE8qAAAAAX6niAMA
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5668167497").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5668167497").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001974381774")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "E_T_L3")
GROUP = getenv("GROUP", "E_T_L3")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


