from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, PING_IMG_URL
from SakkuMusic import app
from SakkuMusic.utils import bot_sys_stats
from SakkuMusic.utils.decorators.language import language

from SakkuMusic.utils.database import get_active_chats, get_active_video_chats

@app.on_message(
    filters.command("respondtostatusbotbaby") & filters.private & ~BANNED_USERS
)
async def respondtobomt(client, message: Message):
    UP, CPU, RAM, DISK = await bot_sys_stats()
    if "%" in CPU:
        CPU = CPU.replace("%", "")
    if "%" in DISK:
        DISK = DISK.replace("%", "")
    active_voice = len(await get_active_chats())
    active_video = len(await get_active_video_chats())
    x = f"{DISK}_+_{CPU}_+_{UP}_+_{active_voice}_+_{active_video}"
    await message.reply_text(x) 
