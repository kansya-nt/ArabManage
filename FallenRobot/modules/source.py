from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention},

ɪ ᴀᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** ᴅʜɪʟ ᴧꝛᴧʙ
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "Store",
                        url="https://t.me/Arabc0de",
                    ),
                ]
            ]
        ),
    )

@pbot.on_message(filters.command(["Store_Tele"]))
async def Store_Tele(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**Hai Mek {message.from_user.mention},

Dibawah ini beberapa jasa bot dan jajanan telegram dari [SI ARAB STORE](https://t.me/Arabc0de)
Silahkan Klik Button Di Bawah.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴅʜɪʟ sɪ ᴧꝛᴧʙ", user_id=OWNER_ID),
                ]
                [
                    InlineKeyboardButton(
                        text="Ubot Premium",
                        callback_data="Ubot_Prem",
                    ),
                    InlineKeyboardButton(
                        text="Bot Telegram",
                        callback_data="Bot_Tele",
                    ),
                ]
            ]
        ),
    )

@pbot.on_message(filters.command(["Ubot_Prem"]))
async def Ubot_Prem(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**Hai Mek {message.from_user.mention},

Ubot Premium adalah userbot simple yang mmudahkan kalian tanpa harus melewati proses deploy yg rumit & dengan modul yang lebih keren serta full emoji premium jika akun anda premium,
Untuk List Userbot Premium SI ARAB STORE bisa kalian cek list di bawah ini :**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴅʜɪʟ sɪ ᴧꝛᴧʙ", user_id=OWNER_ID),
                ]
                [
                    InlineKeyboardButton(text="Ubot Spesial II", url="https://t.me/Spesial02Ubot",
                    ),
                    InlineKeyboardButton(text="Ubot Spesial III", url="https://t.me/Spesial03Ubot",
                    ),
                    InlineKeyboardButton(text="Ubot Spesial IV", url="https://t.me/Spesial04Ubot",
                    ),
                ]
                [
                    InlineKeyboardButton(text="Ubot Ultra I", url="https://t.me/ArabUltraUbot"),
                    InlineKeyboardButton(text="Ubot Ultra II", url="https://t.me/Ultra02Ubot"),
                    InlineKeyboardButton(text="Ubot Ultra III", url="https://t.me/Ultra03Ubot"),
                ]
                [
                    InlineKeyboardButton(text="Kembali", callback_data="Store_Tele"),
                ],
            ]
        ),
    )

@pbot.on_message(filters.command(["Bot_Tele"]))
async def Bot_Tele(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**Hai Mek {message.from_user.mention},

Jasa Deploy Bot Telegram :

• Userbot Gcast/Delayspam -> Rp.25K/bulan
• Fsub/File Share/Bot Asupan -> Rp.30k/bulan(nambah button 10k)
• Bot Musik Ram 4GB -> 100k/bulan
• Bot Musik Ram 8GB -> 150k/bulan
• Bot Manage -> 80k/bulan

Info Selengkapnya Bisa Contact Saya. [ᴅʜɪʟ ᴧꝛᴧʙ](https://t.me/Dhilnihnge)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴅʜɪʟ sɪ ᴧꝛᴧʙ", user_id=OWNER_ID),
                ]
                [
                    InlineKeyboardButton(
                        text="Ubot Premium",
                        callback_data="Ubot_Prem",
                    ),
                ]
                [
                    InlineKeyboardButton(
                        text="Kembali",
                        callback_data="Store_Tele",
                    ),
                ]
            ]
        ),
    )

@pbot.on_message(filters.command(["Str_Gen"]))
async def Str_Gen(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**Hai Mek {message.from_user.mention},

Jika Kalian Ingin Ngambil String Pyrogram, Pyrogram v2, Telethon Bisa Ketikan /genstring.**
""",
    )


__mod_name__ = "Repo"
