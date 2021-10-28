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
from info import BOT_USERNAME, UPDATES_CHANNEL 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
#=======================================================================

logging.basicConfig(level=logging.INFO)


Sam = Client(
   "Sam",
   bot_token=TOKEN,
   api_id=API_ID,
   api_hash=API_HASH
)

#=======================================================================

@Sam.on_message(filters.incoming & filters.command(['start', 'start@{BOT_USERNAME}']))
def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/AwesomeSupportt).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(message.chat.id,
                text="**👋🏻 Hey [{}](tg://user?id={})**\n__This bot you can protect your channel and lock and open media** \n\n Add the bot admin in your channel directly**".format(message.from_user.first_name, message.from_user.id),
	        reply_markup=InlineKeyboardMarkup(
                    [
                        [   
                           InlineKeyboardButton("Updates Channel", url="https://t.me/LaylaList"),
                           InlineKeyboardButton("Support Group", url="https://t.me/AwesomeSupport")
                      ],
                     [
                           InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/HEROGAMERS1")
                     ]
                 ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    client.send_message(message.chat.id,
        text="**👋🏻 Hey [{}](tg://user?id={})**\n__This bot can protect your channel and lock and open media** \n__Add the bot admin in your channel directly**".format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
		[
                    InlineKeyboardButton("Updates Channel", url="https://t.me/LaylaList"),
                    InlineKeyboardButton("Support Group", url="https://t.me/AwesomeSupport")
                ],
                [
                    InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/HEROGAMERS1")	
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
   

   
@Sam.on_message(filters.channel & filters.all)
async def deleter(bot: Client, cmd: Message):
                  await slp(int(TIME))
                  await cmd.delete()
         

#=======================================================================

Sam.run()
print("Userbot Started!")

#=======================================================================
