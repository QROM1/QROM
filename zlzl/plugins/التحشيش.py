import os
import shutil
from asyncio import sleep
import random

from telethon import events

from . import zedub
from ..core.logger import logging
from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id, get_user_from_event
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)
zed_dev = (55265877)
zel_dev = (78083727)

async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رابط الحذف")
async def _(zed):
    await edit_or_reply (zed, "❖ [𝐀𝐍𝐘𝐍𝐌𝐔𝐒 - 𝘿𝙀𝙇𝙀𝙏𝙀](t.me/ANENMUS) 🗑♻️❖\n**𓍹━─━─━─━─𝐀𝐍𝐘𝐍𝐌𝐔𝐒─━─━─━─━𓍻**\n\n **❖│رابـط الحـذف ↬** https://telegram.org/deactivate \n\n\n **❖│بـوت الحـذف¹  ↬** @LC6BOT\n**❖│بـوت الحـذف²  ↬** @DTeLebot\n ")
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="بوت الحذف")
async def _(zed):
    await edit_or_reply (zed, "❖ [𝐀𝐍𝐘𝐍𝐌𝐔𝐒 - 𝘿𝙀𝙇𝙀𝙏𝙀](t.me/ANENMUS) 🗑♻️❖\n**𓍹━─━─━─━─𝐀𝐍𝐘𝐍𝐌𝐔𝐒─━─━─━─━𓍻**\n\n **❖│رابـط الحـذف ↬** https://telegram.org/deactivate \n\n\n **❖│بـوت الحـذف¹  ↬** @LC6BOT\n**❖│بـوت الحـذف²  ↬** @DTeLebot\n ")
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة المطـورين  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**❖╎تم رفعـه كلب 🐕‍🦺**",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع مرتي(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة المطـورين  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المـزه**  [{tag}](tg://user?id={user.id}) \n**❖╎تـم رفعتهـا مـࢪتي\n✾╎ **",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**❖╎تـم رفعـه تـاج 👑🔥**",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع بعيوني(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**❖╎بـعــيـؤونـي😕   [{tag}](tg://user?id={user.id})**",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المستخـدم ** [{tag}](tg://user?id={user.id}) \n**❖╎ بـقـلبـي [{tag}](tg://user?id={user.id})**",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع قلبي(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المستخـدم ** [{tag}](tg://user?id={user.id}) \n**❖╎ بـقـلبـي [{tag}](tg://user?id={user.id})**",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع جريذي(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❐ عـذراً .. لا يمكننـي اهانـة المطـورين  ❏╰**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❐ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**❖╎تـم رفعـه جـࢪيذي 🐀** ",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
@zedub.zed_cmd(pattern="رفع فرخ(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❐ عـذراً .. لا يمكننـي اهانـة المطـورين  ❏╰**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❐ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath,
        f"**❖╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**❖╎تـم رفعـه فـࢪخ 🖕😹**",
    )
########################  ZThon Userbot ~ By: Zelzal (@zzzzl1l)  ########################
ZelzalTHS_cmd = (
    "❖ [𝗦𝗼𝘂𝗿𝗰𝗲 𝐀𝐍𝐘𝐍𝐌𝐔𝐒 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر التحشيش](t.me/ANYNMUS) ❖\n\n"
    "**- اضغـط ع الامـر للنسـخ ثـم قـم بالـرد ع الشخـص** \n\n"
    "**❖** `.اوصف` \n"
    "**❖** `.هينه` \n"
    "**❖** `.نسبه الحب` \n"
    "**❖** `.نسبه الانوثه` \n"
    "**❖** `.نسبه الغباء` \n"
    "**❖** `.نسبه الانحراف` \n"
    "**❖** `.نسبه المثليه` \n"
    "**❖** `.نسبه النجاح` \n"
    "**❖** `.نسبه الكراهيه` \n"
    "**❖** `.رفع تاج` \n"
    "**❖** `.رفع بقلبي` \n"
    "**❖** `.رفع مرتي` \n"
    "**❖** `.رفع صاك` \n"
    "**❖** `.رفع صاكه` \n"
    "**❖** `.رفع حات` \n"
    "**❖** `.رفع حاته` \n"
    "**❖** `.رفع ورع` \n"
    "**❖** `.رفع مزه` \n"
    "**❖** `.رفع مرتبط` \n"
    "**❖** `.رفع مرتبطه` \n"
    "**❖** `.رفع حبيبي` \n"
    "**❖** `.رفع خطيبتي` \n"
    "**❖** `.رفع جلب` \n"
    "**❖** `.رفع جريذي` \n"
    "**❖** `.رفع فرخ` \n"
    "**❖** `.رفع مطي` \n"
    "**❖** `.رفع حمار` \n"
    "**❖** `.رفع خروف` \n"
    "**❖** `.رفع حيوان` \n"
    "**❖** `.رفع بزون` \n"
    "**❖** `.رفع زباله` \n"
    "**❖** `.رفع منشئ` \n"
    "**❖** `.رفع مدير` \n"
    "**❖** `.رفع كواد` \n"
    "🛃 سيتـم اضـافة المزيـد من تخصيص الاوامـر بالتحديثـات الجـايه\n"
)

kettuet = [
"وش أكثر شي يقهرك؟",
"آخر ديره رحت لها؟",
"رح لـ @، وقل له شي بخاطرك؟",
"تغار ولا؟",
"تحس إن فيه أحد يرقبك؟",
"ناس تمنيتهم يبقون، لكن أول ما حسّوا بهالشي ابتعدوا.. قد صارت لك؟",
"انولدت بنفس الديره اللي عايش فيها الحين؟",
"وش الشي اللي يزعلك بسرعه؟",
"تغار ولا تمشيها؟",
"كم حجم ذاكرة جوالك؟",
"وين تخبي أسرارك؟",
"اعترف لـ @ بشي بقلبك؟",
"يومك راح على وش؟",
"أغرب شي صار لك بحياتك؟",
"كم تحب الأكل من ١٠؟",
"وش حكمة دايم تعيش عليها؟",
"وش أكثر شي يرفع ضغطك؟",
"قد ظلمك أحد؟",
"انخنت قبل كذا؟",
"فيه تاريخ غيّر حياتك؟",
"وش أحلى سنة مرت عليك؟",
"نفس مكان ولادتك، هو مكانك الآن؟",
"وش يزعلك؟ ووش يرضيك؟",
"وش هوايتك؟",
"سافرت لدوله وندمت؟",
"منهو اللي تطلع معه وتنبسط؟",
"يعطونك مليون، تضرب خويك؟",
"وش تاريخ ميلادك؟",
"كم مره حبيت؟",
"وش أقوى درس علمتك الحياة؟",
"واثق من نفسك؟",
"كم مره نمت جنب وحده؟",
"وش اسمك الثلاثي؟",
"كلمه لشخص خذلك؟",
"تسامح بسرعه؟",
"وش تسوي إذا زعلت وتبي تروق؟",
"تشرب عصير وإلا قهوه؟",
"تثق بأحد؟",
"كم مره حبيت؟",
"كمل الحديث: قال الرسول ﷺ أنا مدينة العلم و...؟",
"صف حياتك بكلمتين؟",
"حياتك ماتزين بدون مين؟",
"وش روتينك اليومي؟",
"وش تسوي إذا طفشت؟",
"متى عيد ميلادك؟",
"وش سبب أغلب مشاكلك؟",
"تحس أحد يكرهك أو يحقد عليك؟",
"قل كلمه من لهجتك ومعناها؟",
"تحب اسمك؟ ولو بتغيّره وش تختار؟",
"كيف تشوف الجيل ذا؟",
"وش تاريخ ما تنساه أبد؟",
"تقتل أحد علشان الفلوس؟",
"تؤمن بالحب من أول نظره؟",
"صف حياتك بكلمات بسيطه؟",
"طبع يخليك تكره شخص، حتى لو تحبه؟",
"وش نوع الموسيقى اللي تحبها؟ وليه؟",
"كم أطول نومه نمتها؟",
"كلمه من لهجتك ومعناها؟",
"وش تسوي لو مزح معك واحد ماتعرفه؟",
"فيه شخص تحب تستفزه؟",
"الغيره عندك حب ولا أنانيه؟",
"مع أو ضد: النوم أفضل حل للمشاكل؟",
"لو صديقك نوى لك شر، وش موقفك؟",
"للشباب: متى آخر مره بنت غزلتك؟",
"صف نفسك بكلمه؟",
"شي من يومك صغير ما تغيّر فيك؟",
"لو واحد ما تعرفه مزح معك، وش تسوي؟",
"لو شفت شخص عجبك، كيف تبدأ الحديث معه؟",
"كلمه لشخص فرّحك وأنت زعلان؟",
"وش الشي اللي تحس نفسك مبدع فيه؟",
"تهمك الماركات بملابسك؟",
"يومك راح على وش؟",
"لو صديقك طلع حاقد عليك، وش بتسوي؟",
"تقتل أحد علشان الفلوس؟",
"كلمه تمشي معك هالفتره؟",
"وش علوم قلبك؟",
"صريح؟ مشتاق؟",
"أغرب اسم سمعته؟",
"تفضل تكون غبي أو قبيح؟",
"آخر مره أكلت أكلك المفضل؟",
"سافرت لديره وندمت؟",
"وش أشياء صعب تتقبلها بسرعه؟",
"كلمه لشخص غالي اشتقت له؟",
"وش الشي اللي مات في مجتمعنا؟",
"تسامح شخص غلط بحقك وندم؟",
"آخر شي ضاع منك؟",
"الغيره حب ولا أنانيه؟",
"لو جيت تساعد صديق وقالك مالك دخل، وش بتسوي؟",
"وش شي كل ما تذكرته تضحك؟",
"تحب شي، ليه اخترته؟",
"تصرف كل راتبك؟ ولا عندك هدف وتوفر؟",
"متى تكره أحد، حتى لو كنت تحبه؟",
"وش أقبح شي بالعلاقه: الغدر ولا الإهمال؟",
"جتك رساله أثّرت فيك؟",
"تحس أحد يحبك؟",
"وش تسوي إذا زعلت وتبي تطلع حرّتك؟",
"صوت مغني ما تحبه؟",
"كم بحسابك البنكي؟",
"موقف ما تنساه طول عمرك؟",
"ردة فعلك لو مزح معك شخص م تعرفه؟",
"عندك حس فكاهي؟ ولا نكدي؟",
"من وجهة نظرك، وش اللي يقوي العلاقه؟",
"وش نوع الموسيقى اللي تحبها؟ وليه؟",
"توفر فلوسك ولا تصرفها كلها؟",
"جتك رساله غير متوقعه وأثرت فيك؟",
"وش شي ما تغير فيك من الصغر؟",
"تضحي بشي غالي علشان شخص تحبه؟",
"تحب شي، ليه اخترته؟",
"لو صديقك قال مالك دخل، وش بتسوي؟",
"كلمه لشخص أسعدك وانت حزين؟",
"كم مره تسبح باليوم؟",
"أفضل صفه تحبها في نفسك؟",
"أحلى شي صار معك اليوم؟",
"وش شي سمعته ومعلق براسك هاليومين؟",
"تغير صفه فيك علشان شخص تحبه؟",
"وش أحسن صفه في صديقك المقرب؟",
"وش شاغل بالك هالفتره؟",
"آخر مره ضحكت من قلب؟",
"وش أكثر دوله ودك تزورها؟",
"آخر خبر حلو، متى وصلك؟",
"كم نسبة حاجتك للعزله؟",
"توفر ولا تصرف كل راتبك؟",
"وش جمله أثرت فيك؟",
"لو قالوا لك تاكل صنف واحد طول الشهر، وش تختار؟",
"تصرف كل راتبك؟ ولا توفّر لهدف؟",
"متى آخر مره ضحكت من قلب؟",
"وش تطلع فيه زعلك؟",
"متى تكره شخص، حتى لو معجب فيه؟",
"تحس فيه أحد يراقبك؟",
"أحقر الناس هو اللي...؟",
"وش شي من صغرك ما تغير؟",
"من وجهة نظرك، وين تلقى السعاده؟",
"تغار من أصحابك؟",
"وش أكثر جمله أثرت فيك؟",
"كم شخص معطيه بلوك؟",
"وش أحلى سنة مرت عليك؟",
"صف نفسك بكلمه؟",
]

wasf = [
    "لا خلقۿ ولا اخلاق لحاله عايش ☹.",
    "سڪر محلي محطوط على ڪريما 🤤🍰.",
    "؏ـسل × ؏ـسل 🍯.",
    "أنسان مرتب وڪشاخ بس مشكلتۿ يجذب هواي 😂.",
    "ملڪ جمال ألعالم 🥺💘.",
    "أنسان زباله ومكضيها نوم 🙂.",
    "يعني بشرفك هوه هذا يستاهل اوصفه؟",
    "أنسان ڪيمر 😞💘.",
    "جنۿ جڪليته يربيـﮧ 🍬.",
    "شمأ اوصف بي قليل 🥵💞.",
    "وجۿا جنة كاهي من ألصبحـﮧ ☹♥.",
    "هذا واحد يهودي دير بالك منه 🙂💘.",
    "هذا انسان يحب مقتدئ ابتعد عنه 😂💞.",
    "بس تزحف ع الولد وهيه زرڪة 😂.",
    "جنۿ مرڪة شجر شبيك يول 😂😔.",
    "هذا حبيبي ، أحبة ڪولش 🙊💘",
    "جمالهـﮧ خبلني 😞💞.",
    "چنۿ ڪريمة ؏ـلى ڪيك 😞💘.",
    "انسان مينطاق 🙂💔.",
    "فد أنسان مرتب وريحتة تخبل 🥺💞",
    "شڪد حلو هذا ومؤدب 😭💞💘💕.",
    "وفف مو بشر ضيم لضيعه من ايدڪك نصيحة 🥺💞.",
    "نتا مخلوق من ڪتله مال عارية 🙂😂.",
    "لضيعۿ من أيدك خوش أنسانن وحباب رتبط بي احسلڪك 🥺.",
    "با؏ هذا الصاڪك يربي شنو مخلوق منعسل 🥺🧿.",
    "شني عمي مو بشر ڪيك ورب 🥺💞.",
    "عوفه ضلعي هذا انسان زباله 🙂😂.",
    "انسان ساقط لتحجي وياه انطي بلوڪك بدون تفاهم 🙂🤦‍♀️.",
    "باع منو شون بشر هوه وجۿا يطرد النعمة 🙂.",
    "عيع فد أنسان وصخ 😂♥.",
    "يول هذا طاڪك قطة احسلك 😂💞.",
    "لازم واحد يضمه بقوطيه ويقفل عليه لان هالبشر ڪيك 🤤💘.",
    "هذا الله غاضب عليه 🌚💔.",
    "شنو شنو ؟ تسرسح يله 😒💘.",
    "وردة مال الله ، فدوا اروحله 🤤💞.",
    "أنسان مؤدب من البيت للجامع ، ومن الجامع للبيت 😞💞.",
    "انسان بومة وبس نايم مدري شلون اهله ساكتيله 🌚💞.",
    "أنت شايف وجها من يكعد الصبح ؟ عمي خلينا ساكتين 🙂😂.",
    "الله وكيلك هذا اهله كلشي ممستافدين من عنده 🥲💞.",
    "لكشنو من جمالل هذا يربييييي 😭💞.",
    "يومة فديته جنه زربه 😭😂💞.",
]

heno = [
    " لاتتكلم مع أسيادك كذا فاهم؟ ",
    "تعال يابن الشاررع اليوم انعل والديك",
    "ياحيوان ياقواد اصمل ",
]

mth = [
    "100٪ يحبك ويخاف عليك بصدق.",
    "100٪ يحبك ويخشى عليك من كل شيء.",
    "91٪ جزء كبير من قلبه لك.",
    "81٪ يعشقك بجنون.",
    "81٪ مغرم بك ولا يرى غيرك.",
    "40٪ شخص أناني لا يهتم إلا بمصلحته، ابتعد عنه.",
    "50٪ فكّر جيداً في علاقتك به.",
    "30٪ خائن، حاولي أن تتركيه، لا نفع منه.",
    "25٪ يواعد غيرك ويكذب عليك بالحب.",
    "25٪ شخص سيء الطباع، اتركيه فوراً.",
    "0٪ لا يحبك بل يزعجك.",
    "0٪ لا يحبك بل يكرهك.",
]

zid = [
    "100%",
    "99%",
    "98%",
    "97%",
    "96%",
    "95%",
    "90%",
    "89%",
    "88%",
    "87%",
    "86%",
    "85%",
    "80%",
    "79%",
    "78%",
    "77%",
    "76%",
    "75%",
    "70%",
    "69%",
    "68%",
    "67%",
    "66%",
    "65%",
    "60%",
    "59%",
    "58%",
    "57%",
    "56%",
    "55%",
    "50%",
    "48%",
    "47%",
    "46%",
    "45%",
    "40%",
    "39%",
    "38%",
    "37%",
    "36%",
    "35%",
    "30%",
    "29%",
    "28%",
    "27%",
    "25%",
    "20%",
    "19%",
    "18%",
    "17%",
    "16%",
    "15%",
    "10%",
    "9%",
    "8%",
    "7%",
    "6%",
    "5%",
    "4%",
    "3%",
    "2%",
    "1%",
    "0%",

]

@zedub.zed_cmd(pattern="كت(?: |$)(.*)")
async def ahmed(ahmed): # Code Update by @zzzzl1l
    zelzal = ahmed.pattern_match.group(1)
    zilzal = await ahmed.get_reply_message()
    zel_zal = random.choice(kettuet)
    if not zilzal and not zelzal: # Code Update by @zzzzl1l
        return await edit_or_reply(ahmed, f"**❖╎{zel_zal}**")
    user, custom = await get_user_from_event(ahmed)
    if not user: # Code Update by @zzzzl1l
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    if custom: # Code Update by @zzzzl1l
        zedth2 = custom
    me = await ahmed.client.get_me()
    my_first = me.first_name
    my_ahmed = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(ahmed, f"**⌔╎لـ  ** [{zedth2}](tg://user?id={user.id}) \n**⌔╎{zel_zal}**")

@zedub.zed_cmd(pattern="(نسبه الحب|نسبة الحب)(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(mth)
    await edit_or_reply(malath, f"**❖╎نـسبـة حبكـم انـت و**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 😻♥️**")

@zedub.zed_cmd(pattern="(نسبه الانوثة|نسبة الانوثه|نسبه الانوثه|نسبة الانوثة)(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(malath, f"**✾❖╎نسبـة الانوثه لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤰**")

@zedub.zed_cmd(pattern="(نسبه الغباء|نسبة الغباء)(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(malath, f"**❖╎نسبـة الغبـاء لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 😂💔**")

@zedub.zed_cmd(pattern="(نسبه الانحراف|نسبة الانحراف)(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(malath, f"**✾╎نسبـة الانحـراف لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🥵🖤**")

@zedub.zed_cmd(pattern="(نسبه المثليه|نسبة المثليه)(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(malath, f"**❖ نسبـة المثليـه لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🏳️‍🌈.**")

@zedub.zed_cmd(pattern="(نسبه النجاح|نسبة النجاح)(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(malath, f"**❖╎نسبـة النجـاح لـ** [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤓.**") 

@zedub.zed_cmd(pattern="(نسبه الكراهية|نسبة الكراهيه|نسبه الكراهيه|نسبة الكراهية)(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(malath, f"**✾╎نسبـة الكراهيـة لـ** [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤮.**")

@zedub.zed_cmd(pattern="رفع ورع(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎تم رفعـه ورع القـروب 😹.**")

@zedub.zed_cmd(pattern="رفع مزه(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚺 ╎ الحلـوه ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـها مـزة الكروب 🥳💃.**")

@zedub.zed_cmd(pattern="رفع مطي(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مطي سبورتي 🐴.** \n")

@zedub.zed_cmd(pattern="رفع حمار(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حمار  😂🐴.** \n")

@zedub.zed_cmd(pattern="رفع خروف(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه خـروف 🐑.** \n")

@zedub.zed_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    if custom:
        return await edit_or_reply(malath, f"[{custom}](tg://user?id={user.id})")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **🐑╎ تم رفعـه حيـوان .** \n")

@zedub.zed_cmd(pattern="رفع بزون(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    if custom:
        return await edit_or_reply(malath, f"[{custom}](tg://user?id={user.id})")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        malath, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **🐈╎ تم رفعـه بـزون .** \n"
    )

@zedub.zed_cmd(pattern="رفع زباله(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه زباله  🗑.** \n")

@zedub.zed_cmd(pattern="رفع منشئ(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه منشئ القروب 👷‍♂️.** \n")

@zedub.zed_cmd(pattern="رفع مدير(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مدير القروب 🤵‍♂️.** \n")

@zedub.zed_cmd(pattern="رفع قواد(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه قواد .. بنجـاح 👀. ** \n")

@zedub.zed_cmd(pattern="رفع مرتبط(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ المستخـدم  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـه مرتبـط .. بنجـاح 💍💞** \n")

@zedub.zed_cmd(pattern="رفع مرتبطه(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"** ╎ الحلـوه ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـهـا مرتبطـه .. بنجـاح 💍💞. .** \n")

@zedub.zed_cmd(pattern="رفع حبيبي(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"**🚹 ╎ الحلـو  ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حبيبـج .. بنجـاح 💍🤵‍♂👰🏻‍♀.**")

@zedub.zed_cmd(pattern="رفع خطيبتي(?: |$)(.*)")
async def zed(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(malath, f"** ╎ الحلـوه ❖ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـهـا خطيبتك .. بنجـاح 💍👰🏼‍♀️.** \n")

@zedub.zed_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖  هـذا مطـوري . .  ما اقدر اوصفه 😞  ❏╰**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ تعال نيكني حبيبي قرم  🙊💘 ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    owsf = random.choice(wasf)
    await edit_or_reply(malath, f"**- {owsf}**")

@zedub.zed_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(malath):
    user, custom = await get_user_from_event(malath)
    if not user:
        return
    if user.id in zed_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـورين السـورس  ❖**")
    if user.id in zel_dev:
        return await edit_or_reply(malath, f"**╮ ❖ عـذراً .. لا يمكننـي اهانـة مطـور السـورس  ❖**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    hah = random.choice(heno)
    await edit_or_reply(malath, f"**- {hah}**")

# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="التحشيش")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalTHS_cmd)
