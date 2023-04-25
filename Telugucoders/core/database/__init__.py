""" mongo database """

from motor.motor_asyncio import AsyncIOMotorClient as Amala
from config import MONGODB_URL as tmo


MONGODB_CLI = Amala(tmo)
db = MONGODB_CLI.plugins

