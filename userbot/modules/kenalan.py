from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^Ms(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`𝐀𝐋𝐈𝐀𝐍𝐒𝐈 𝐌𝐈𝐌𝐈𝐊 𝐒𝐔𝐒𝐔`")
    sleep(1)
    await typew.edit("𝐎𝐖𝐍𝐄𝐑: 𝐒𝐄𝐌𝐏𝐀𝐊 𝐁𝐄𝐒𝐈`")
    sleep(1)
    await typew.edit("`𝐋𝐔 𝐁𝐄𝐋𝐔𝐌 𝐊𝐄𝐑𝐄𝐍 𝐊𝐀𝐋𝐎 𝐁𝐄𝐋𝐔𝐌 𝐊𝐄𝐍𝐀𝐋 𝐌𝐒, 𝐒𝐈𝐍𝐈 𝐒𝐔𝐉𝐔𝐃 𝐃𝐔𝐋𝐔!!!`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
