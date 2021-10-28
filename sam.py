#👀

import pyrogram
import asyncio
import logging
import os

from asyncio import sleep as slp
from pyrogram import Client, filters
from pyrogram.types import User, Message

from info import API_ID
from info import API_HASH
from info import ADMINS
from info import TOKEN
from info import TIME
from info import GROUPS
#=======================================================================

logging.basicConfig(level=logging.INFO)


Sam = Client(
   "Sam",
   bot_token=TOKEN,
   api_id=API_ID,
   api_hash=API_HASH
)

#=======================================================================

@Sam.on_message(filters.group & filters.all)
async def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  await slp(int(TIME))
                  await cmd.delete()

#=======================================================================

Sam.run()
print("Userbot Started!")

#=======================================================================
