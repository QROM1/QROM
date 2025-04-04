#ZedThon

import asyncio
import os
import time
from datetime import datetime

from . import zedub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import progress, reply_id

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"

blocked_word = ["وقتي", "الوقتي", "تلقائي", "التلقائي"]

@zedub.zed_cmd(pattern="rename (.*)")
async def _(event):
    if event.fwd_from:
        return
    zedevent = await edit_or_reply(
        event,
        "**💈جـارِ إعادة تسميـة الـميديا ▬▭ ..🪙𓆰**\n\n**❖❖قد يستغرق الأمر بضع دقـائق إذا كان حجـم الملف كبيـراً**",
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        c_time = time.time()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await event.client.download_media(
            reply_message,
            downloaded_file_name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, zedevent, c_time, "جـارِ التنزيـل...", file_name)
            ),
        )
        end = datetime.now()
        ms = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            await zedevent.edit(
                f"**File Downloaded in {ms} seconds.**\n**File location : **`{downloaded_file_name}`"
            )
        else:
            await zedevent.edit("Error Occurred\n {}".format(input_str))
    else:
        await zedevent.edit(
            "**Syntax : ** `.rename file.name` as reply to a Telegram media"
        )


@zedub.zed_cmd(pattern="إسم (.*)")
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    zedevent = await edit_or_reply(
        event,
        "**❖❖جـارِ إعادة تسميـة الـميديا ▬▭ ...💈**\n\n**❖❖قد يستغرق الأمر بضع دقـائق إذا كان حجـم الملف كبيـراً**",
    )
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        c_time = time.time()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await event.client.download_media(
            reply_message,
            downloaded_file_name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, zedevent, c_time, "جـارِ التنزيـل...", file_name)
            ),
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            caat = await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_to_id,
                thumb=thumb,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, event, c_time, "جـارِ الـرفـع...", downloaded_file_name
                    )
                ),
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await zedevent.edit(
                f"**❖❖** {ms_one} **ثوان.**\n**تم التنزيل في** {ms_two} **ثوان.**"
            )
            await asyncio.sleep(3)
            await zedevent.delete()
        else:
            await zedevent.edit("File Not Found {}".format(input_str))


@zedub.zed_cmd(pattern="اسم (.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    if input_str in blocked_word:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    zedevent = await edit_or_reply(
        event,
        "**⌔∮جـارِ إعادة تسميـة الـميديا ▬▭ ...💈**❖❖قد يستغرق الأمر بضع دقـائق إذا كان حجـم الملف كبيـراً**",
    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        c_time = time.time()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await event.client.download_media(
            reply_message,
            downloaded_file_name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, zedevent, c_time, "جـارِ التنزيـل...", file_name)
            ),
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            caat = await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=reply_to_id,
                thumb=thumb,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, event, c_time, "جـارِ الـرفـع...", downloaded_file_name
                    )
                ),
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await zedevent.edit(
                f"**❖❖** {ms_one} **ثوان.**\n**تم التنزيل في** {ms_two} **ثوان.**"
            )
            await asyncio.sleep(3)
            await zedevent.delete()
        else:
            await zedevent.edit("File Not Found {}".format(input_str))

