from pyrogram import filters
from pyrogram.types import Message

from SakkuMusic import app
from SakkuMusic.misc import SUDOERS
from SakkuMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto End Stream Enabled.\n\nBot will leave voice chat automatically after 3 mins if no one is listening with a warning message.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto End Stream Disabled.")
    else:
        await message.reply_text(usage)
