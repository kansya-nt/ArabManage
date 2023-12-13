
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from FallenRobot import OWNER_ID, 
from FallenRobot import *

query = update.callback_query
UbotPrem = """
**ʜᴇʏ {message.from_user.mention} 
UBot Premium adalah Userbot dengan fitur yang di sesuaikan dan di permudah untuk masalah deployment.
Dan Ubot Premium Support Segala Macam Emoji Premium di Dalam Modulnya

• Bot Premium -> Rp.30k/bulan
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Dhil Arab", user_id=OWNER_ID),
                ]
                 [
                    InlineKeyboardButton(
                        "Arab Ultra Ubot",
                        url="https://t.me/ArabUltraUbot",
                    InlineKeyboardButton(
                        "Arab Spesial Ubot",
                        url="https://t.me/Spesial02Ubot",
                    ),
                ]
                 [
                    InlineKeyboardButton("Kembali", callback_data="source_back"),
                ]
            ]
        ),

if query.data == "source_back":
        first_name = update.effective_user.first_name
        query.message.edit_text(
            PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,
            disable_web_page_preview=True,
        )

