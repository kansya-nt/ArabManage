#Coded By: @Dhilnihnge
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from FallenRobot import OWNER_ID, source_back,

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


