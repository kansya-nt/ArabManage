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

from FallenRobot import SUPPORT_CHAT

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ʙᴜᴀᴛ sᴛʀɪɴɢ", callback_data="gensession")],
        )

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)



@pbot.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "gensession":
        return await cq.message.reply_text(
            text="<b>» ᴋʟɪᴋ ᴘᴀᴅᴀ ᴛᴏᴍʙᴏʟ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ sᴛʀɪɴɢ ᴀɴᴅᴀ :</b>",
            reply_markup=gen_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await gen_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await gen_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await gen_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)

async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» ʟᴀɢɪ ᴄᴏʙᴀ {ty} ɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ ᴀɴᴅᴀ...")

    try:
        api_id = await dispatcher.bot.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀsᴜᴋɪɴ ᴀᴘɪ ɪᴅ ʟᴜ ʙᴜʀᴜ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await update.effective_message.reply_text("» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await update.effective_message.reply_text("» ᴀᴘɪ ɪᴅ ʟᴜ sᴀʟᴀʜ ʙʟᴏɢ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await dispatcher.bot.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀsᴜᴋɪɴ ᴀᴘɪ ʜᴀsʜ ʟᴜ ʙᴜʀᴜ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await update.effective_message.reply_text("» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await update.effective_message.reply_text("» ᴀᴘɪ ʜᴀsʜ ʟᴜ sᴀʟᴀʜ ʙʟᴏɢ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await dispatcher.bot.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀsᴜᴋɪɴ ɴᴏᴍᴏʀ ᴛᴇʟᴇ ʟᴜ ʙᴜʀᴜ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await update.effective_message.reply_text("» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await update.effective_message.reply_text("» ʟᴀɢɪ ɴʏᴏʙᴀ ɴɢɪʀɪᴍɪɴ ᴏᴛᴘ ᴋᴇ ᴀᴋᴜɴ ʟᴜ...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="pbot", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await update.effective_message.reply_text("» ɢᴀɢᴀʟ ɴɢɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ ᴋᴇ ᴀᴋᴜɴ ʟᴜ.\n\nʜᴀʀᴀᴘ ᴛᴜɴɢɢᴜ {f.value or f.x} sᴇᴄᴏɴᴅs ᴅᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await update.effective_message.reply_text("» ᴀᴘɪ ʜᴀsʜ ᴀᴛᴀᴜ ᴀᴘɪ ɪᴅ ʟᴜ sᴀʟᴀʜ ʙʟᴏɢ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await update.effective_message.reply_text("» ᴍᴀsᴜᴋɪɴ ɴᴏᴍᴏʀ ᴛᴇʟᴇ sᴀʟᴀʜ ʙʟᴏɢ ʟᴜ\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    try:
        otp = await dispatcher.bot.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"ᴍᴀsᴜᴋɪɴ ᴋᴏᴅᴇ ᴏᴛᴘ ʟᴜ ᴅᴀʀɪ ɴᴏᴍᴏʀ {phone_number}.\n\nᴋᴀʟᴏ ᴋᴏᴅᴇ ᴏᴛᴘɴʏᴀ <code>12345</code>, ᴛᴏʟᴏɴɢ ᴋɪʀɪᴍᴋᴀɴ sᴇᴘᴇʀᴛɪ ɪɴɪ <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await update.effective_message.reply_text("» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 10 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await update.effective_message.reply_text("» <b>ᴋᴏᴅᴇ ᴏᴛᴘ ʏɢ ʟᴜ ᴍᴀsᴜᴋɪɴ sᴀʟᴀʜ.</b>\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await update.effective_message.reply_text("» <b>ᴋᴏᴅᴇ ᴏᴛᴘ ʏɢ ʟᴜ ᴍᴀsᴜᴋɪɴ ᴇxᴘɪʀᴇᴅ.</b>\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await dispatcher.bot.ask(
                identifier=(message.chat.id, user_id, None),
                text="» ᴍᴀsᴜᴋɪɴ ᴘᴡ ᴠᴇʀɪғ 𝟸 ʟᴀɴɢᴋᴀʜ ʟᴜ :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return update.effective_message.reply_text("» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await update.effective_message.reply_text("» ᴘᴡ ᴠᴇʀɪғ 𝟸 ʟᴀɴɢᴋᴀʜ ʟᴜ sᴀʟᴀʜ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await update.effective_message.reply_text(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "ɴɪʜ {0} sᴛʀɪɴɢ sᴇssɪᴏɴ ʟᴜ\n\n<code>{1}</code>\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={2}>sɪ ᴧꝛᴧʙ</a>\n☠ <b>ɴᴏᴛᴇ :</b> Jᴀɴɢᴀɴ ʟᴜ sᴇʙᴀʀɪɴ ʙᴜᴀᴛ ᴘɪɴJᴏʟ."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@Arabc0de"))
            await client(JoinChannelRequest("@Cehaarab"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("SiArab_Support")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await update.effective_message.reply_text("ɴɪʜ sᴛʀɪɴɢ ʟᴜ ᴜᴅᴀʜ Jᴀᴅɪ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\nᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ʟᴜ ʏᴀɴɢ ʙᴀɴʏᴀᴋ ʙᴏᴋᴇᴘɴʏᴀ.\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={SUPPORT_CHAT}>sɪ ᴧꝛᴧʙ</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ʟᴜ",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» ɴɢᴇʙᴀᴛᴀʟɪɴ ᴘʀᴏsᴇs ɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ ʟᴜ.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» sᴜᴋsᴇs ɴɢᴇʀᴇsᴛᴀʀᴛ ʙᴏᴛ.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    else:
        return False
