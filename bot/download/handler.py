from os.path import isfile
from random import choices, randint
from string import ascii_letters, digits
from time import time

from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message

from .. import folder
from .manager import downloads
from .type import Download


async def addFile(_, msg: Message):
    caption = msg.caption or ""
    filename = folder.get() + '/'
    if caption[:1] == '>':
        filename += caption[2:]
    else:
        try:
            media = getattr(msg, msg.media.value)
            filename += media.file_name
        except AttributeError:
            filename += ''.join(choices(ascii_letters+digits, k=12))
    if isfile(filename):
        await msg.reply("File already exists!", quote=True)
        return
    waiting = await msg.reply(
        f"File __{filename}__ added to list.",
        quote=True,
        parse_mode=ParseMode.MARKDOWN
    )
    downloads.append(Download(
        id=randint(int(1e9), int(1e10-1)),
        filename=filename,
        from_message=msg,
        added=time(),
        progress_message=waiting
    ))
