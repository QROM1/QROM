import asyncio
from pathlib import Path
import os
import glob
import random
import requests

from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    NodeJSNotInstalled,
    NotInGroupCallError,
    TooOldNodeJSVersion,
)
from pytgcalls.types import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
from telethon import functions
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChannelInvalidError
from yt_dlp import YoutubeDL

from .stream_helper import Stream, check_url, video_dl, yt_regex
from ..Config import Config

vc_session = Config.VC_SESSION

def get_cookies_file():
    folder_path = f"{os.getcwd()}/zion"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    return cookie_txt_file


class ZedVC:
    def __init__(self, client) -> None:
        self.app = PyTgCalls(client, overload_quiet_mode=True)
        self.client = client
        self.CHAT_ID = None
        self.CHAT_NAME = None
        self.PLAYING = False
        self.PAUSED = False
        self.MUTED = False
        self.PLAYLIST = []

    async def start(self):
        await self.app.start()

    def clear_vars(self):
        self.CHAT_ID = None
        self.CHAT_NAME = None
        self.PLAYING = False
        self.PAUSED = False
        self.MUTED = False
        self.PLAYLIST = []

    async def join_vc(self, chat, join_as=None):
        if self.CHAT_ID:
            try:
                await self.app.leave_group_call(self.CHAT_ID)
            except (NotInGroupCallError, NoActiveGroupCall):
                pass
            self.CHAT_NAME = None
            self.CHAT_ID = None
            self.PLAYING = False
            self.PLAYLIST = []
            #return f"⚈ **مـوجـود بالفعـل بالمحـادثـه الصـوتيـه عـلى** {self.CHAT_NAME}"
        if join_as:
            try:
                join_as_chat = await self.client.get_entity(int(join_as))
                join_as_title = f" كـ **{join_as_chat.title}**"
            except ValueError:
                return "❖ **قم باضافة ايدي المجموعه لامر الانضمام**"
        else:
            join_as_chat = await self.client.get_me()
            join_as_title = ""
        try:
            await self.app.join_group_call(
                chat_id=chat.id,
                stream=AudioPiped("zedthon/ahmed/Silence01s.mp3"),
                join_as=join_as_chat,
                stream_type=StreamType().pulse_stream,
            )
        except NoActiveGroupCall:
            if vc_session:
                try:
                    await self.client(
                        functions.phone.CreateGroupCallRequest(
                            peer=chat,
                            title="مكالمة صوتيه",
                        )
                    )
                    await self.join_vc(chat=chat, join_as=join_as)
                except ChatAdminRequiredError:
                    return "❖ **انت بحاجه الى صلاحيات المشـرف✖️**\n❖ **لـ بـدء محـادثه صـوتيـه هنـا 🤷🏻‍♀**\n❖ **او قم بطلب من احـد المشـرفين هنـا**"
                except ChannelInvalidError:
                    return "❖ **لديك حساب مساعد للميوزك قمت بتعيينه سابقاً**\n❖**\n❖ **ثم قم بفتح المكالمه في المجموعة**"
            else:
                try:
                    await self.client(
                        functions.phone.CreateGroupCallRequest(
                            peer=chat,
                            title="مكالمة صوتيه",
                        )
                    )
                    await self.join_vc(chat=chat, join_as=join_as)
                except ChatAdminRequiredError:
                    return "❖ **انت بحاجه الى صلاحيات المشـرف✖️**\n❖ **لـ بـدء محـادثه صـوتيـه هنـا 🤷🏻‍♀**\n⚉ **او قم بطلب من احـد المشـرفين هنـا**"
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return "- آخـر اصـدار من NodeJs لم يتـم تحميلـه ...؟!"
        except AlreadyJoinedError:
            await self.app.leave_group_call(chat.id)
            await asyncio.sleep(3)
            await self.join_vc(chat=chat, join_as=join_as)
        self.CHAT_ID = chat.id
        self.CHAT_NAME = chat.title
        if vc_session:
            return f"⚉ **تم الانضمـام بنجـاح ✓**\n❖ **الى المكالمـة ⤌ ⎞** {chat.title} **⎝** - {join_as_title}\n❖ **الانضمام:** عبر الحساب المساعـد"
        else:
            return f"⚉ **تم الانضمـام بنجـاح ✓**\n❖ **الى المكالمـة ⤌ ⎞** {chat.title} **⎝** - {join_as_title}"

    async def leave_vc(self):
        try:
            await self.app.leave_group_call(self.CHAT_ID)
        except (NotInGroupCallError, NoActiveGroupCall):
            pass
        self.CHAT_NAME = None
        self.CHAT_ID = None
        self.PLAYING = False
        self.PLAYLIST = []

    async def play_song(self, input, stream=Stream.audio, force=False):
        if yt_regex.match(input):
            with YoutubeDL({"no-playlist": True, "cookiefile": get_cookies_file()}) as ytdl:
                ytdl_data = ytdl.extract_info(input, download=False)
                title = ytdl_data.get("title", None)
            if title:
                playable = await video_dl(input, title)
            else:
                return "❖ **خطـأ بجلب الرابـط**"
        elif check_url(input):
            try:
                res = requests.get(input, allow_redirects=True, stream=True)
                ctype = res.headers.get("Content-Type")
                if "video" not in ctype or "audio" not in ctype:
                    return "❖ **رابـط غيـر صالـح ✘**"
                name = res.headers.get("Content-Disposition", None)
                if name:
                    title = name.split('="')[0].split('"') or ""
                else:
                    title = input
                playable = input
            except Exception as e:
                return f"❖ **رابـط غيـر صـالح :**\n\n{e}"
        else:
            path = Path(input)
            if path.exists():
                if not path.name.endswith(
                    (".mkv", ".mp4", ".webm", ".m4v", ".mp3", ".flac", ".wav", ".m4a")
                ):
                    return "❖ **ملف غيـر صـالح لتشغيـله**"
                playable = str(path.absolute())
                title = path.name
            else:
                return "❖ **مسـار الملـف غيـر موجـود ؟!**"
        print(playable)
        if self.PLAYING and not force:
            self.PLAYLIST.append({"title": title, "path": playable, "stream": stream})
            return f"❖ **تم الاضـافه لـ قـائمـة التشغيـل ✓**\n❖ **المـوقـع:** {len(self.PLAYLIST)+1}"
        if not self.PLAYING:
            self.PLAYLIST.append({"title": title, "path": playable, "stream": stream})
            await self.skip()
            if vc_session:
                return f"❖ **تم التشغيـل .. بنجـاح 🎶**\n❖ **العنـوان:** `{title}`\n❖ **التشغيـل:** عبر الحساب المساعـد\n❖ **لـ عـرض اوامـر الميـوزك ⇜⎞** `.ميوزك` **⎝**"
            else:
                return f"❖ **تم التشغيـل .. بنجـاح 🎶**\n❖ **العنـوان:** `{title}`\n❖ **لـ عـرض اوامـر الميـوزك ⇜⎞** `.ميوزك` **⎝**"
        if force and self.PLAYING:
            self.PLAYLIST.insert(
                0, {"title": title, "path": playable, "stream": stream}
            )
            await self.skip()
            if vc_session:
                return f"❖ **تم التشغيـل .. بنجـاح 🎶**\n❖ **العنـوان:** `{title}`\n❖ **التشغيـل:** عبر الحساب المساعـد\n❖ **لـ عـرض اوامـر الميـوزك ⇜⎞** `.ميوزك` **⎝**"
            else:
                return f"❖ **تم التشغيـل .. بنجـاح 🎶**\n❖ **العنـوان:** `{title}`\n❖ **لـ عـرض اوامـر الميـوزك ⇜⎞** `.ميوزك` **⎝**"

    async def handle_next(self, update):
        if isinstance(update, StreamAudioEnded):
            await self.skip()

    async def skip(self, clear=False):
        if clear:
            self.PLAYLIST = []

        if not self.PLAYLIST:
            if self.PLAYING:
                await self.app.change_stream(
                    self.CHAT_ID,
                    AudioPiped("zedthon/ahmed/Silence01s.mp3"),
                )
            self.PLAYING = False
            return "❖ **التخطـي 💈**\n❖ **عـذراً عـزيـزي ❖**\n❖ **قائمـة الشغيـل فارغـه ؟!**"

        next = self.PLAYLIST.pop(0)
        if next["stream"] == Stream.audio:
            streamable = AudioPiped(next["path"])
        else:
            streamable = AudioVideoPiped(next["path"])
        try:
            await self.app.change_stream(self.CHAT_ID, streamable)
        except Exception:
            await self.skip()
        self.PLAYING = next
        if vc_session:
            return f"❖ **تم التخطـي 💈**\n❖ **تم تشغيـل التالي .. بنجـاح 💈**\n❖ **العنـوان:** `{next['title']}`\n❖ **التشغيـل:** عبر الحساب المساعـد\n\n❖ **لـ عـرض اوامـر الميـوزك ⇜⎞** `.ميوزك` **⎝**"
        else:
            return f"❖ **تم التخطـي 💈**\n❖ **تم تشغيـل التالي .. بنجـاح 💈**\n❖ **العنـوان:** `{next['title']}`\n\n❖ **لـ عـرض اوامـر الميـوزك ⇜⎞** `.ميوزك` **⎝**"

    async def pause(self):
        if not self.PLAYING:
            return "❖ **عـذراً عـزيـزي ✗**\n❖ **لايـوجـد شـي لـ الايقـاف ؟!**"
        if not self.PAUSED:
            await self.app.pause_stream(self.CHAT_ID)
            self.PAUSED = True
        return f"❖ **تم التمهـل في** {self.CHAT_NAME}"

    async def resume(self):
        if not self.PLAYING:
            return "❖ **عـذراً عـزيـزي ✗**\n❖ **لايـوجـد شـي لـ الاستئنـاف ؟!**"
        if self.PAUSED:
            await self.app.resume_stream(self.CHAT_ID)
            self.PAUSED = False
        return f"❖ **تم الاستئنـاف في**  {self.CHAT_NAME}"

    # async def mute(self):
    #     if not self.PLAYING:
    #         return "Nothing is playing to Mute"
    #     if not self.MUTED:
    #         await self.app.mute_stream(self.CHAT_ID)
    #         self.PAUSED = True
    #     return f"Muted Stream on {self.CHAT_NAME}"

    # async def unmute(self):
    #     if not self.PLAYING:
    #         return "Nothing is playing to Unmute"
    #     if self.MUTED:
    #         await self.app.unmute_stream(self.CHAT_ID)
    #         self.MUTED = False
    #     return f"Unmuted Stream on {self.CHAT_NAME}"
