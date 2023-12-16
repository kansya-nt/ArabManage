import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)

from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from FallenRobot.config import API_HASH, API_ID
from FallenRobot import Anony

ask_ques = "**» Silakan pilih library yang ingin Anda hasilkan stringnya :**\n\nNote: Saya tidak mengumpulkan informasi pribadi apa pun dari fitur ini, Anda dapat menggunakan bot sendiri jika Anda mau."
buttons_ques = [
    [
        InlineKeyboardButton("Pyrogram v2", callback_data="pyrogram"),
        InlineKeyboardButton("Telethon", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot"),
        InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [InlineKeyboardButton(text="Ambil String", callback_data="genstring")]
]


async def is_batal(msg):
    if msg.text == "/cancel":
        await msg.reply(
            "**» Membatalkan proses pembuatan sesi string yang sedang berlangsung !**",
            quote=True,
            reply_markup=InlineKeyboardMarkup(gen_button),
        )
        return True
    elif msg.text == "/skip":
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply(
            "**» Membatalkan proses pembuatan sesi string yang sedang berlangsung!**",
            quote=True,
        )
        return True
    else:
        return False


@pbot.on_callback_query(
    filters.regex(pattern=r"^(genstring|pyrogram|pyrogram_bot|telethon_bot|telethon)$")
)
async def callbackgenstring(bot, callback_query):
    query = callback_query.matches[0].group(1)
    if query == "genstring":
        await callback_query.answer()
        await callback_query.message.reply(
            ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques)
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram_bot":
                await callback_query.answer(
                    "» Generator sesinya adalah Pyrogram v2.", show_alert=True
                )
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(
                    bot, callback_query.message, telethon=True, is_bot=True
                )
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            LOGGER.error(traceback.format_exc())
            ERROR_MESSAGE = (
                "Something went wrong. \n\n**ERROR** : {} "
                "\n\n**Please forward this message to my Owner**, if this message "
                "doesn't contain any sensitive data "
                "because this error is **not logged by bot.** !"
            )
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


@pbot.on_message(
    filters.private & ~filters.forwarded & filters.command("genstring")
)
async def genstringg(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot, msg, telethon=False, is_bot: bool = False):
    ty = "Telethon" if telethon else "Pyrogram"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"» Mencoba untuk memulai **{ty}** generator string...")
    api_id_msg = await msg.chat.ask(
        " **API_ID** to proceed.\n\nClick on /skip for using bot's api.",
        filters=filters.text,
    )
    if await is_batal(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = API_ID
        api_hash = API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
            await api_id_msg.delete()
        except ValueError:
            return await api_id_msg.reply(
                "Tolong kirimkan **API_ID** harus bilangan bulat, mulailah membuat sesi Anda lagi.",
                quote=True,
                reply_markup=InlineKeyboardMarkup(gen_button),
            )
        api_hash_msg = await msg.chat.ask(
            "» Tolong kirimkan **API_HASH** untuk melanjutkan.", filters=filters.text
        )
        if await is_batal(api_hash_msg):
            return
        api_hash = api_hash_msg.text
        await api_hash_msg.delete()
    t = (
        "Please send your **BOT_TOKEN** to continue.\nExample : `5432198765:abcdanonymousterabaaplol`'"
        if is_bot
        else "» Tolong kirimkan **PHONE_NUMBER** dengan kode negara yang ingin Anda buat sesinya. \nContoh : `+6286356837789`'"
    )
    phone_number_msg = await msg.chat.ask(t, filters=filters.text)
    if await is_batal(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    await phone_number_msg.delete()
    if not is_bot:
        await msg.reply("» Mencoba mengirim OTP ke nomor yang diberikan...")
    else:
        await msg.reply("» Trying to login using Bot Token...")
    if telethon and is_bot or telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(
            name="bot",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=phone_number,
            in_memory=True,
        )
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        return await msg.reply(
            "» **API_ID** dan **API_HASH** kombinasinya tidak cocok. \n\nSilakan mulai membuat string Anda lagi.",
            reply_markup=InlineKeyboardMarkup(gen_button),
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        return await msg.reply(
            "» **PHONE_NUMBER** Anda bukan anggota akun mana pun di Telegram.\n\nSilakan mulai membuat sesi Anda lagi.",
            reply_markup=InlineKeyboardMarkup(gen_button),
        )
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await msg.chat.ask(
                "» tolong kirimkan **OTP** Yang Anda terima dari Telegram di akun Anda.\nJika OTP `12345`, **tolong kirimkan dengan format** `1 2 3 4 5`.",
                filters=filters.text,
                timeout=600,
            )
            if await is_batal(phone_code_msg):
                return
    except ListenerTimeout:
        return await msg.reply(
            "» Batas waktu mencapai 10 menit.\n\nSilakan mulai membuat sesi Anda lagi.",
            reply_markup=InlineKeyboardMarkup(gen_button),
        )
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        await phone_code_msg.delete()
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            return await msg.reply(
                "» OTP yang Anda kirim adalah **salah.**\n\nSilakan mulai membuat sesi Anda lagi.",
                reply_markup=InlineKeyboardMarkup(gen_button),
            )
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            return await msg.reply(
                "» OTP yang Anda kirim adalah **expired.**\n\nSilakan mulai membuat sesi Anda lagi.",
                reply_markup=InlineKeyboardMarkup(gen_button),
            )
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await msg.chat.ask(
                    "» Silakan masukkan **Two Step Verification** pwnya untuk melanjutkan.",
                    filters=filters.text,
                    timeout=300,
                )
            except ListenerTimeout:
                return await msg.reply(
                    "» Batas waktu mencapai 5 menit.\n\nSilakan mulai membuat sesi Anda lagi.",
                    reply_markup=InlineKeyboardMarkup(gen_button),
                )
            try:
                password = two_step_msg.text
                await two_step_msg.delete()
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await is_batal(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                return await two_step_msg.reply(
                    "» Kata sandi yang Anda kirimkan salah.\n\nSilakan mulai membuat sesi lagi.",
                    quote=True,
                    reply_markup=InlineKeyboardMarkup(gen_button),
                )
    elif telethon:
        try:
            await client.start(bot_token=phone_number)
        except Exception as err:
            return await msg.reply(err)
            
        try:
            await client.sign_in_bot(phone_number)
        except Exception as err:
            return await msg.reply(err)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**Ini adalah {ty} Sesi String Anda** \n\n`{string_session}` \n\n**Dihasilkan Oleh :** @{bot.me.username}\n• **Catatan :** Don jangan share ke siapapun Bahkan ke pacar kalian sendiri hehe"
    try:
        if not is_bot:
            await client.send_message("me", text)
            await client(JoinChannelRequest("@Arabc0de"))
            await client(JoinChannelRequest("@Cehaarab"))
            await client.join_chat("SiArab_Support")
        else:
            await bot.send_message(msg.chat.id, text)
            await client(JoinChannelRequest("@Arabc0de"))
            await client(JoinChannelRequest("@Cehaarab"))
            await client.join_chat("SiArab_Support")
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(
        msg.chat.id,
        f'» Berhasil membuat file Anda {"Telethon" if telethon else "Pyrogram"} Sesi String.\n\nSilakan periksa pesan tersimpan  kalian yang banyak aib nya untuk mendapatkannya! \n\n**A String Generator bot by ** @Dhilnihnge',
    )



__mod_name__ = "Gen String"

__help__ = """
Untuk Mengambil String Session PyrogramV2 & Telethon

 ♜ /genstring*:* Untuk Mengambil String.


"""
