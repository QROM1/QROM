import requests
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from . import zedub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

ANYNMUS_cmd = (
    "❖ [SOURCE 𝐀𝐍𝐘𝐍𝐌𝐔𝐒 - كاشف الأرقام العربية](t.me/ANYNMUS) ❖\n\n"
    "**❖ الأمر ↵**\n\n"
    "❖ `.اكشف` + الرقم مع مفتاح الدولة\n\n"
    "**❖ الوصف :**\n"
    "**- لجلب قائمة بأسماء صاحب رقم هاتف معين**\n\n"
)

@zedub.zed_cmd(pattern="اكشف(?: |$)([\s\S]*)")
async def _(event):
    number = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not number and reply:
        number = reply.text
    if not number:
        return await edit_delete(event, "**- الرقم خطأ أو لم تقم بإدخال كود الدولة +**", 10)
    if "+" not in number:
        return await edit_delete(
            event, "**- الرقم خطأ أو لم تقم بإدخال كود الدولة +**", 10
        )

    bot_username = "@ydysgsgsbot"
    zed = await edit_or_reply(event, "**❖ جارِ الكشـف عن الرقم 📲**\n**❖ انتظر قليلاً ... ▬▭**")
    
    async with borg.conversation(bot_username) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(number)
            response = await conv.get_response()
            await borg.send_message(event.chat_id, response)
            await zed.delete()
        except YouBlockedUserError:
            await zedub(unblock("ZZIIIbot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(number)
            response = await conv.get_response()
            await borg.send_message(event.chat_id, response)
            await zed.delete()


@zedub.zed_cmd(pattern="الكاشف")
async def cmd(event):
    await edit_or_reply(event, ANYNMUS_cmd)