import asyncio

from . import zedub
from ..core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete
from ..helpers.tools import media_type
from ..helpers.utils import _format
from ..sql_helper import no_log_pms_sql
from ..sql_helper.globals import addgvar, gvarstatus, delgvar
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
plugin_category = "البوت"

class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0

LOG_CHATS_ = LOG_CHATS()

@zedub.zed_cmd(incoming=True, func=lambda e: e.is_private, edited=False, forword=None)
async def monito_p_m_s(event):  # sourcery no-metrics
    if Config.PM_LOGGER_GROUP_ID == -100:
        return
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        return
    sender = await event.get_sender()
    if not sender.bot:
        chat = await event.get_chat()
        fullname = f"{sender.first_name}{sender.last_name}" if sender.last_name else sender.first_name #Write Code By T.me/ZThon
        user_name = f"@{sender.username}" if sender.username else "لا يوجـد" #Write Code By T.me/ZThon
        if not no_log_pms_sql.is_approved(chat.id) and chat.id != 777000:
            if LOG_CHATS_.RECENT_USER != chat.id:
                LOG_CHATS_.RECENT_USER = chat.id
                if LOG_CHATS_.NEWPM:
                    LOG_CHATS_.COUNT = 0
                LOG_CHATS_.NEWPM = await event.client.send_message(
                    Config.PM_LOGGER_GROUP_ID,
                    f"**❖┊المسـتخـدم :** {_format.mentionuser(fullname, sender.id)} .\n**❖┊الايـدي :** `{chat.id}`\n**❖┊اليـوزر :** {user_name}\n\n**❖┊قام بـ إرسـال رسائـل جـديـده**",
                )
            try:
                if event.message:
                    await event.client.forward_messages(
                        Config.PM_LOGGER_GROUP_ID, event.message, silent=True
                    )
                LOG_CHATS_.COUNT += 1
            except Exception as e:
                LOGS.warn(str(e))

@zedub.zed_cmd(incoming=True, func=lambda e: e.mentioned, edited=False, forword=None)
async def log_tagged_messages(event):
    from .afk import AFK_

    if gvarstatus("GRPLOG") and gvarstatus("GRPLOG") == "false":
        return
    if gvarstatus("GRPLOG") and gvarstatus("GRPLOG") != "false":
        hmm = await event.get_chat()
        if (
            (no_log_pms_sql.is_approved(hmm.id))
            or (Config.PM_LOGGER_GROUP_ID == -100)
            or ("on" in AFK_.USERAFK_ON)
            or (await event.get_sender() and (await event.get_sender()).bot)
        ):
            return
        full = None
        try:
            full = await event.client.get_entity(event.message.from_id)
        except Exception as e:
            LOGS.info(str(e))
        messaget = await media_type(event)
        resalt = f"#التــاكــات\n\n<b>❖ معـلومـات المجمـوعـة :</b>"
        resalt += f"\n<b>❖ الاسـم : </b> {hmm.title}"
        resalt += f"\n<b>❖ الايـدي : </b> <code>{hmm.id}</code>"
        if full is not None:
            fullusername = f"@{full.username}" if full.username else "لايوجد" #Write Code By T.me/ZThon
            fullid = full.id
            fullname = f"{full.first_name} {full.last_name}" if full.last_name else full.first_name
            resalt += f"\n\n<b>❖ معـلومـات المـرسـل :</b>"
            resalt += f"\n<b>❖ الاسـم : </b> {fullname}"
            resalt += f"\n<b>❖ الايـدي : </b> <code>{fullid}</code>"
            resalt += f"\n<b>❖ اليـوزر : </b> {fullusername}" #Write Code By T.me/ZThon
        if messaget is not None:
            resalt += f"\n\n<b>❖ رسـالـة ميـديـا : </b><code>{messaget}</code>"
        else:
            resalt += f"\n\n<b>❖ الرســالـه : </b>{event.message.message}"
        resalt += f"\n\n<b>❖ رابـط الرسـاله : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> اضغـط هنـا</a>"
        if not event.is_private:
            await event.client.send_message(
                Config.PM_LOGGER_GROUP_ID,
                resalt,
                parse_mode="html",
                link_preview=False,
            )
            try:
                await event.client.forward_messages(
                    Config.PM_LOGGER_GROUP_ID, event.message, silent=True
                )
            except Exception as e:
                LOGS.warn(str(e))

@zedub.zed_cmd(
    pattern="خزن(?:\s|$)([\s\S]*)",
    command=("خزن", plugin_category),
    info={
        "header": "To log the replied message to bot log group so you can check later.",
        "الاسـتخـدام": [
            "{tr}خزن",
        ],
    },
)
async def log(log_text):
    "To log the replied message to bot log group"
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#التخــزين / ايـدي الدردشــه : {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit("**❖ بالــرد على اي رسـاله لحفظهـا في كـروب التخــزين**")
            return
        await log_text.edit("**❖ تـم الحفـظ في كـروب التخـزين .. بنجـاح ✓**")
    else:
        await log_text.edit("**❖ عـذراً .. هـذا الامـر يتطلـب تفعيـل فـار التخـزين اولاً**")
    await asyncio.sleep(2)
    await log_text.delete()

@zedub.zed_cmd(
    pattern="تفعيل التخزين$",
    command=("تفعيل التخزين", plugin_category),
    info={
        "header": "To turn on logging of messages from that chat.",
        "الاسـتخـدام": [
            "{tr}log",
        ],
    },
)
async def set_no_log_p_m(event):
    "To turn on logging of messages from that chat."
    if Config.PM_LOGGER_GROUP_ID != -100:
        chat = await event.get_chat()
        if no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.disapprove(chat.id)
            await edit_delete(
                event, "**❖ تـم تفعيـل التخـزين لهـذه الدردشـه .. بنجـاح ✓**", 5
            )

@zedub.zed_cmd(
    pattern="تعطيل التخزين$",
    command=("تعطيل التخزين", plugin_category),
    info={
        "header": "To turn off logging of messages from that chat.",
        "الاسـتخـدام": [
            "{tr}nolog",
        ],
    },
)
async def set_no_log_p_m(event):
    "To turn off logging of messages from that chat."
    if Config.PM_LOGGER_GROUP_ID != -100:
        chat = await event.get_chat()
        if not no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.approve(chat.id)
            await edit_delete(
                event, "**⌔ تـم تعطيـل التخـزين لهـذه الدردشـه .. بنجـاح ✓**", 5
            )

@zedub.zed_cmd(
    pattern="تخزين الخاص (تفعيل|تعطيل)$",
    command=("تخزين الخاص", plugin_category),
    info={
        "header": "To turn on or turn off logging of Private messages in pmlogger group.",
        "الاسـتخـدام": [
            "{tr}pmlog on",
            "{tr}pmlog off",
        ],
    },
)
async def set_pmlog(event):
    "To turn on or turn off logging of Private messages"
    if Config.PM_LOGGER_GROUP_ID == -100:
        return await edit_delete(
            event,
            "__For functioning of this you need to set PM_LOGGER_GROUP_ID in config vars__",
            10,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "تعطيل":
        h_type = False
    elif input_str == "تفعيل":
        h_type = True
    PMLOG = gvarstatus("PMLOG") and gvarstatus("PMLOG") != "false"
    if PMLOG:
        if h_type:
            addgvar("PMLOG", h_type)
            await event.edit("**- تخزين الخاص بالفعـل ممكـن ✓**")
        else:
            addgvar("PMLOG", h_type)
            await event.edit("**- تـم تعطيـل تخـزين رسـائل الخـاص .. بنجـاح✓**")
    elif h_type:
        addgvar("PMLOG", h_type)
        await event.edit("**- تـم تفعيـل تخـزين رسـائل الخـاص .. بنجـاح✓**")
    else:
        addgvar("PMLOG", h_type)
        await event.edit("**- تخزين الخاص بالفعـل معطـل ✓**")

@zedub.zed_cmd(
    pattern="تخزين القروبات (تفعيل|تعطيل)$",
    command=("تخزين القروبات", plugin_category),
    info={
        "header": "To turn on or turn off group tags logging in pmlogger group.",
        "الاسـتخـدام": [
            "{tr}grplog on",
            "{tr}grplog off",
        ],
    },
)
async def set_grplog(event):
    "To turn on or turn off group tags logging"
    if Config.PM_LOGGER_GROUP_ID == -100:
        return await edit_delete(
            event,
            "__For functioning of this you need to set PM_LOGGER_GROUP_ID in config vars__",
            10,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "تعطيل":
        h_type = False
    elif input_str == "تفعيل":
        h_type = True
    GRPLOG = gvarstatus("GRPLOG") and gvarstatus("GRPLOG") != "false"
    if GRPLOG:
        if h_type:
            addgvar("GRPLOG", h_type)
            addgvar("GRPLOOG", h_type)
            await event.edit("**- تخزين القروبات بالفعـل ممكـن ✓**")
        else:
            addgvar("GRPLOG", h_type)
            delgvar("GRPLOOG")
            await event.edit("**- تـم تعطيـل تخـزين منشن القروبات .. بنجـاح✓**")
    elif h_type:
        addgvar("GRPLOG", h_type)
        addgvar("GRPLOOG", h_type)
        await event.edit("**- تـم تفعيـل تخـزين منشن القروبات .. بنجـاح✓**")
    else:
        addgvar("GRPLOG", h_type)
        delgvar("GRPLOOG")
        await event.edit("**- تخزين القروبات بالفعـل معطـل ✓**")
