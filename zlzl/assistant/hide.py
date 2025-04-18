import json
import os
import re

from telethon.events import CallbackQuery

from zlzl import zedub


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"hide_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./zlzl/hide.txt"):
        jsondata = json.load(open("./zlzl/hide.txt"))
        try:
            reply_pop_up_alert = jsondata[f"{timestamp}"]["text"]
        except KeyError:
            reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في سيـرفرات الانينمـَوس"
    else:
        reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في سيـرفرات الانينمـَوس"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
