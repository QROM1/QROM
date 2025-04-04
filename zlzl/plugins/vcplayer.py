# تحديث فريق زدثــون
# ZThon T.me/ZedThon
# Devolper ZelZal T.me/zzzzl1l
import asyncio
import logging

from youtube_search import YoutubeSearch
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import User
from . import zedub
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

from ..vc_zelzal.stream_helper import Stream
from ..vc_zelzal.tg_downloader import tg_dl
from ..vc_zelzal.vcp_helper import ZedVC

plugin_category = "المكالمات"

logging.getLogger("pytgcalls").setLevel(logging.ERROR)

OWNER_ID = zedub.uid

vc_session = Config.VC_SESSION

if vc_session:
    vc_client = TelegramClient(
        StringSession(vc_session), Config.APP_ID, Config.API_HASH
    )
else:
    vc_client = zedub

vc_client.__class__.__module__ = "telethon.client.telegramclient"
vc_player = ZedVC(vc_client)

asyncio.create_task(vc_player.start())


@vc_player.app.on_stream_end()
async def handler(_, update):
    await vc_player.handle_next(update)


ALLOWED_USERS = set()


@zedub.zed_cmd(
    pattern="انضمام ?(\S+)? ?(?:ك)? ?(\S+)?",
    command=("انضمام", plugin_category),
    info={
        "header": "لـ الانضمـام الى المحـادثه الصـوتيـه",
        "ملاحظـه": "يمكنك اضافة الامر (ك) للامر الاساسي للانضمام الى المحادثه ك قنـاة مع اخفاء هويتك",
        "امـر اضافـي": {
            "ك": "للانضمام الى المحادثه ك قنـاة",
        },
        "الاستخـدام": [
            "{tr}انضمام",
            "{tr}انضمام + ايـدي المجمـوعـه",
            "{tr}انضمام ك (peer_id)",
            "{tr}انضمام (chat_id) ك (peer_id)",
        ],
        "مثــال :": [
            "{tr}انضمام",
            "{tr}انضمام -1005895485",
            "{tr}انضمام ك -1005895485",
            "{tr}انضمام -1005895485 ك -1005895485",
        ],
    },
)
async def joinVoicechat(event):
    "لـ الانضمـام الى المحـادثه الصـوتيـه"
    chat = event.pattern_match.group(1)
    joinas = event.pattern_match.group(2)

    await edit_or_reply(event, "❖ **جـارِ الانضمـام الى المكالمـة الصـوتيـه ...**")

    if chat and chat != "ك":
        if chat.strip("-").isnumeric():
            chat = int(chat)
    else:
        chat = event.chat_id

    if vc_player.app.active_calls:
        return await edit_delete(
            event, f"❖ **انت منضـم مسبقـاً الـى**  {vc_player.CHAT_NAME}"
        )

    try:
        vc_chat = await zedub.get_entity(chat)
    except Exception as e:
        return await edit_delete(event, f'❖ **خطـأ** : \n{e or "UNKNOWN CHAT"}')

    if isinstance(vc_chat, User):
        return await edit_delete(event, "❖ **عـذراً عـزيـزي ✗**\n❖ **المكالمـة الصـوتيـه مغلقـه هنـا ؟!**\n❖ **قم بفتح المكالمـه اولاً 🗣**")

    if joinas and not vc_chat.username:
        await edit_or_reply(event, "❖ **عـذراً عـزيـزي**\n❖**لم استطـع الانضمـام الى المكالمـة ✗**\n❖ **قم بالانضمـام يدويـاً**")
        joinas = False

    out = await vc_player.join_vc(vc_chat, joinas)
    await edit_delete(event, out)


@zedub.zed_cmd(
    pattern="خروج",
    command=("خروج", plugin_category),
    info={
        "header": "لـ المغـادره من المحـادثه الصـوتيـه",
        "الاستخـدام": [
            "{tr}خروج",
        ],
    },
)
async def leaveVoicechat(event):
    "لـ المغـادره من المحـادثه الصـوتيـه"
    if vc_player.CHAT_ID:
        await edit_or_reply(event, "❖ **جـارِ مغـادرة المحـادثـة الصـوتيـه ...**")
        chat_name = vc_player.CHAT_NAME
        await vc_player.leave_vc()
        await edit_delete(event, f"❖ **تم مغـادرة المكـالمـه** {chat_name}")
    else:
        await edit_delete(event, "❖ **لم تنضم بعـد للمكالمـه ؟!**")


@zedub.zed_cmd(
    pattern="قائمة التشغيل",
    command=("قائمة التشغيل", plugin_category),
    info={
        "header": "لـ جلب كـل المقـاطع المضـافه لقائمـة التشغيـل في المكالمـه",
        "الاستخـدام": [
            "{tr}قائمة التشغيل",
        ],
    },
)
async def get_playlist(event):
    "لـ جلب كـل المقـاطع المضـافه لقائمـة التشغيـل في المكالمـه"
    await edit_or_reply(event, "❖ **جـارِ جلب قائمـة التشغيـل ...**")
    playl = vc_player.PLAYLIST
    if not playl:
        await edit_delete(event, "Playlist empty", time=10)
    else:
        zed = ""
        for num, item in enumerate(playl, 1):
            if item["stream"] == Stream.audio:
                zed += f"{num}-  `{item['title']}`\n"
            else:
                zed += f"{num}- `{item['title']}`\n"
        await edit_delete(event, f"❖ **قائمـة التشغيـل :**\n\n{zed}\n**Enjoy the show**")


@zedub.zed_cmd(
    pattern="شغل فيديو ?(1)? ?([\S ]*)?",
    command=("شغل فيديو", plugin_category),
    info={
        "header": "تشغيـل مقـاطع الفيـديـو في المكـالمـات",
        "امـر اضافـي": {
            "1": "فرض تشغيـل المقطـع بالقـوة",
        },
        "الاستخـدام": [
            "{tr}شغل فيديو بالــرد ع فيـديـو",
            "{tr}شغل فيديو + رابـط",
            "{tr}شغل فيديو  ف + رابـط",
        ],
        "مثــال :": [
            "{tr}شغل فيديو بالـرد",
            "{tr}شغل فيديو https://www.youtube.com/watch?v=c05GBLT_Ds0",
            "{tr}شغل فيديو 1 https://www.youtube.com/watch?v=c05GBLT_Ds0",
        ],
    },
)
async def play_video(event):
    "لـ تشغيـل مقـاطع الفيـديـو في المكـالمـات"
    #con = event.pattern_match.group(1).lower()
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    if flag == "يو":
        return
    photo = None
    if input_str and not input_str.startswith("http"):
        try:
            results = YoutubeSearch(input_str, max_results=1).to_dict()
            input_str = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"][:40]
            thumbnail = results[0]["thumbnails"][0]
            #thumb_name = f"{title}.jpg"
            #thumb = requests.get(thumbnail, allow_redirects=True)
            #try:
                #open(thumb_name, "wb").write(thumb.content)
            #except Exception:
                #thumb_name = None
                #pass
            duration = results[0]["duration"]
            photo = thumbnail
        except Exception as e:
            await edit_or_reply(event, f"⚈ **فشـل التحميـل** \n⚈ **الخطأ :** `{str(e)}`")
            return
        zzz = await edit_or_reply(event, "**╮ جـارِ تشغيـل المقطـٓـع الصـٓـوتي في المكـالمـه... ╰**")
        if flag:
            resp = await vc_player.play_song(input_str, Stream.video, force=True)
        else:
            resp = await vc_player.play_song(input_str, Stream.video, force=False)
        if resp:
            if photo:
                try:
                    await event.client.send_file(
                        event.chat_id,
                        photo,
                        caption=resp,
                        link_preview=False,
                        force_document=False,
                    )
                    return await zzz.delete()
                except TypeError:
                    return await zzz.edit(reap)

    if input_str == "" and event.reply_to_msg_id:
        input_str = await tg_dl(event)
    if not input_str:
        return await edit_delete(
            event, "❖ **قـم بـ إدخـال رابـط مقطع الفيديـو للتشغيـل...**", time=20
        )
    if not vc_player.CHAT_ID:
        return await edit_or_reply(event, "❖ **قـم بالانضمـام اولاً الى المكالمـه عبـر الامـر .انضمام**")
    if not input_str:
        return await edit_or_reply(event, "❖ **استخـدم الامـر هكـذا**\n• (`.شغل فيديو` + **اسم مقطع الفيديو**)\n**• او**\n• (`.شغل فيديو` + **رابـط مقطع الفيديو**")
    await edit_or_reply(event, "**╮ جـارِ تشغيـل مقطـٓـع الفيـٓـديو في المكـالمـه... ╰**")
    if flag:
        resp = await vc_player.play_song(input_str, Stream.video, force=True)
    else:
        resp = await vc_player.play_song(input_str, Stream.video, force=False)
    if resp:
        await edit_delete(event, resp, time=30)


@zedub.zed_cmd(
    pattern="شغل ?(1)? ?([\S ]*)?",
    command=("شغل", plugin_category),
    info={
        "header": "تشغيـل المقـاطع الصـوتيـه في المكـالمـات",
        "امـر اضافـي": {
            "1": "فرض تشغيـل المقطـع بالقـوة",
        },
        "الاستخـدام": [
            "{tr}شغل بالــرد ع مقطـع صـوتي",
            "{tr}شغل + رابـط",
            "{tr}شغل 1 + رابـط",
        ],
        "مثــال :": [
            "{tr}شغل بالـرد",
            "{tr}شغل https://www.youtube.com/watch?v=c05GBLT_Ds0",
            "{tr}شغل 1 https://www.youtube.com/watch?v=c05GBLT_Ds0",
        ],
    },
)
async def play_audio(event):
    "لـ تشغيـل المقـاطع الصـوتيـه في المكـالمـات"
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    photo = None
    if input_str and input_str.startswith("فيديو"):
        return
    if input_str and not input_str.startswith("http"):
        try:
            results = YoutubeSearch(input_str, max_results=1).to_dict()
            input_str = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"][:40]
            thumbnail = results[0]["thumbnails"][0]
            #thumb_name = f"{title}.jpg"
            #thumb = requests.get(thumbnail, allow_redirects=True)
            #try:
                #open(thumb_name, "wb").write(thumb.content)
            #except Exception:
                #thumb_name = None
                #pass
            duration = results[0]["duration"]
            photo = thumbnail
        except Exception as e:
            await edit_or_reply(event, f"❖ **فشـل التحميـل** \n❖ **الخطأ :** `{str(e)}`")
            return
        zzz = await edit_or_reply(event, "**╮ جـارِ تشغيـل المقطـٓـع الصـٓـوتي في المكـالمـه... ╰**")
        if flag:
            resp = await vc_player.play_song(input_str, Stream.audio, force=True)
        else:
            resp = await vc_player.play_song(input_str, Stream.audio, force=False)
        if resp:
            if photo:
                try:
                    await event.client.send_file(
                        event.chat_id,
                        photo,
                        caption=resp,
                        link_preview=False,
                        force_document=False,
                    )
                    return await zzz.delete()
                except TypeError:
                    return await zzz.edit(resp)

    if input_str == "" and event.reply_to_msg_id:
        input_str = await tg_dl(event)
    if not input_str:
        return await edit_delete(
            event, "❖ **قـم بـ إدخـال رابـط المقطـع الصوتـي للتشغيـل...**", time=20
        )
    if not vc_player.CHAT_ID:
        return await edit_or_reply(event, "❖ **قـم بالانضمـام الى المكالمـه اولاً**\n⚈ **عبـر الامـر ⤌ ⎞** `.انضمام` **⎝**")
    if not input_str:
        return await edit_or_reply(event, "❖ **استخـدم الامـر هكـذا**\n• (`.شغل` + **اسم المقطع الصوتي**)\n**• او**\n• (`.شغل` + **رابـط المقطع الصوتي**")
    await edit_or_reply(event, "**╮ جـارِ تشغيـل المقطـٓـع الصـٓـوتي في المكـالمـه... ╰**")
    if flag:
        resp = await vc_player.play_song(input_str, Stream.audio, force=True)
    else:
        resp = await vc_player.play_song(input_str, Stream.audio, force=False)
    if resp:
        await edit_delete(event, resp, time=30)


@zedub.zed_cmd(
    pattern="توقف",
    command=("توقف", plugin_category),
    info={
        "header": "لـ ايقـاف تشغيـل للمقطـع مؤقتـاً في المكـالمـه",
        "الاستخـدام": [
            "{tr}تمهل",
        ],
    },
)
async def pause_stream(event):
    "لـ ايقـاف تشغيـل للمقطـع مؤقتـاً في المكـالمـه"
    await edit_or_reply(event, "⚈ **جـارِ الايقـاف مؤقتـاً ...**")
    res = await vc_player.pause()
    await edit_delete(event, res, time=30)


@zedub.zed_cmd(
    pattern="كمل",
    command=("كمل", plugin_category),
    info={
        "header": "لـ متابعـة تشغيـل المقطـع في المكـالمـه",
        "الاستخـدام": [
            "{tr}تابع",
        ],
    },
)
async def resume_stream(event):
    "لـ متابعـة تشغيـل المقطـع في المكـالمـه"
    await edit_or_reply(event, "⚈ **جـار الاستئنـاف ...**")
    res = await vc_player.resume()
    await edit_delete(event, res, time=30)


@zedub.zed_cmd(
    pattern="تخطي",
    command=("تخطي", plugin_category),
    info={
        "header": "لـ تخطي تشغيـل المقطـع وتشغيـل المقطـع التالـي في المكـالمـه",
        "الاستخـدام": [
            "{tr}تخطي",
        ],
    },
)
async def skip_stream(event):
    "لـ تخطي تشغيـل المقطـع وتشغيـل المقطـع التالـي في المكـالمـه"
    await edit_or_reply(event, "❖ **جـار التخطـي ...**")
    res = await vc_player.skip()
    await edit_delete(event, res, time=30)


ZelzalMusic_cmd = (
"[ᯓ 𝐀𝐍𝐘𝐍𝐌𝐔𝐒 𝙱𝙾𝚃 - اوامــر الميـوزك 🎸](t.me/ANENMUS) ."
"**⋆─┄─┄─┄─┄──┄─┄─┄─┄─⋆**\n"
"❖ `.شغل`\n"
"**⪼ الامـر + (كلمـة او رابـط) او بالـرد ع مقطـع صوتـي**\n"
"❖ `.شغل فيديو`\n"
"**⪼ الامـر + (كلمـة او رابـط) او بالـرد ع مقطـع فيديـو**\n\n"
"**Ⓜ️ اوامـر تشغيـل اجباريـه مـع تخطـي قائمـة التشغيـل :**\n"
"❖ `.شغل 1`\n"
"**⪼ الامـر + (كلمـة او رابـط) او بالـرد ع مقطـع صوتـي**\n"
"❖ `.شغل فيديو 1`\n"
"**⪼ الامـر + (كلمـة او رابـط) او بالـرد ع مقطـع فيديـو**\n\n"
"❖ `.قائمة التشغيل`\n"
"❖ `.توقف`\n"
"❖ `.كمل`\n"
"❖ `.تخطي`\n\n"
"❖ `.انضمام`\n"
"❖ `.خروج`\n\n"
"❖ `.اضف فار مساعد الميوزك`\n"
"**⪼ الامـر بالـرد ع كـود تيليثون حساب مساعد الميوزك الجديـد**\n\n"
)

@zedub.zed_cmd(pattern="الميوزك")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalMusic_cmd)

@zedub.zed_cmd(pattern="ميوزك")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalMusic_cmd)


"""
@zedub.zed_cmd(
    pattern="a(?:llow)?vc ?([\d ]*)?",
    command=("allowvc", plugin_category),
    info={
        "header": "To allow a user to control VC.",
        "الوصـف": "To allow a user to controll VC.",
        "الاستخـدام": [
            "{tr}allowvc",
            "{tr}allowvc (user id)",
        ],
    },
)
async def allowvc(event):
    "To allow a user to controll VC."
    user_id = event.pattern_match.group(1)
    if user_id:
        user_id = user_id.split(" ")
    if not user_id and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        user_id = [reply.from_id]
    if not user_id:
        return await edit_delete(event, "Whom should i Add")
    ALLOWED_USERS.update(user_id)
    return await edit_delete(event, "Added User to Allowed List")


@zedub.zed_cmd(
    pattern="d(?:isallow)?vc ?([\d ]*)?",
    command=("disallowvc", plugin_category),
    info={
        "header": "To disallowvc a user to control VC.",
        "الوصـف": "To disallowvc a user to controll VC.",
        "الاستخـدام": [
            "{tr}disallowvc",
            "{tr}disallowvc (user id)",
        ],
    },
)
async def disallowvc(event):
    "To allow a user to controll VC."
    user_id = event.pattern_match.group(1)
    if user_id:
        user_id = user_id.split(" ")
    if not user_id and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        user_id = [reply.from_id]
    if not user_id:
        return await edit_delete(event, "Whom should i remove")
    ALLOWED_USERS.difference_update(user_id)
    return await edit_delete(event, "Removed User to Allowed List")


@zedub.on(
    events.NewMessage(outgoing=True, pattern=f"{tr}(speak|sp)(h|j)?(?:\s|$)([\s\S]*)")
)  #only for zedub client
async def speak(event):
    "Speak in vc"
    r = event.pattern_match.group(2)
    input_str = event.pattern_match.group(3)
    re = await event.get_reply_message()
    if ";" in input_str:
        lan, text = input_str.split(";")
    else:
        if input_str:
            text = input_str
        elif re and re.text and not input_str:
            text = re.message
        else:
            return await event.delete()
        if r == "h":
            lan = "hi"
        elif r == "j":
            lan = "ja"
        else:
            lan = "en"
    text = deEmojify(text.strip())
    lan = lan.strip()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    file = "./temp/" + "voice.ogg"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(file)
        cmd = [
            "ffmpeg",
            "-i",
            file,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            file + ".opus",
        ]
        try:
            t_response = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await edit_or_reply(event, str(exc))
        else:
            os.remove(file)
            file = file + ".opus"
        await vc_player.play_song(file, Stream.audio, force=False)
        await event.delete()
        os.remove(file)
    except Exception as e:
         await edit_or_reply(event, f"**Error:**\n`{e}`")
"""
