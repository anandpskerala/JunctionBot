from pyrogram import filters
from pyrogram.types import Message
from bot import JunctionBot


@JunctionBot.on_message(filters.command("start") & filters.incoming & filters.private)
async def _(c: JunctionBot, m: Message):
    await m.reply_text(
        "Hi {} I am a Junction Bot. I can forward messages from one chat to multiple chats",
        parse_mode="markdown",
        reply_to_message_id=m.message_id
    )
