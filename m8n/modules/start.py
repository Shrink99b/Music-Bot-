import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from m8n.utils.filters import command

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import BOT_NAME



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        text=f"""ʜᴇʏ ʜᴀɪ 🥀\n\n๏ ᴛʜɪs ɪɪs {BOT_NAME} 🫧 !\n➻ ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.\n\n──────────────────\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "❄️ ᴀʙᴏᴜᴛ ❄️", callback_data="others"),
                    InlineKeyboardButton(
                        "✨ sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/Namma_Pasanga_Tamil_Chating")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🥀", url=f"https://t.me/AboutSarathi")
                ]
           ]
        ),
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def gcstart(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"Thanks for adding me in your group !! If you want to use me with right actions promote me as admin in this Chat.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 Bot Owner", url=f"https://t.me/{OWNER_USERNAME}")
                ]
            ]
        ),
    )
