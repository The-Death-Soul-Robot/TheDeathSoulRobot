import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](t.me/The_Death_Soul_Robot) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [𝑯𝒖𝒔𝒔𝒂𝒊𝒏](t.me/Love_Dear_Comrades) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» ☠️☠️☠️ «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🕊️ ʀᴇᴘᴏꜱɪᴛᴏʀʏ🕊️", url=f"https://github.com/The-Death-Soul-Robot/TheDeathSoulRobot"),
      ],[
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ 💜", url="https://t.me/Love_Dear_Comrades"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
