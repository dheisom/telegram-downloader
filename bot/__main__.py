from threading import Thread

from pyrogram import idle
from pyrogram.filters import command, document, media
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
from pyrogram.handlers.message_handler import MessageHandler

from . import app, commands
from .download.handler import addFile
from .download.manager import stopDownload
from .download.manager import run as downloadRunner
from .util import checkAdmins

app.add_handler(MessageHandler(
    checkAdmins(commands.start),
    command('start')
))
app.add_handler(MessageHandler(
    checkAdmins(commands.botHelp),
    command('help')
))
app.add_handler(MessageHandler(
    checkAdmins(commands.usage),
    command('usage')
))
app.add_handler(MessageHandler(
    checkAdmins(commands.infoCmd),
    command('info')
))
app.add_handler(MessageHandler(
    checkAdmins(commands.useFolder),
    command('use')
    ))
app.add_handler(MessageHandler(
    checkAdmins(commands.leaveFolder),
    command('leave')
))
app.add_handler(MessageHandler(
    checkAdmins(addFile),
    document | media
))
app.add_handler(CallbackQueryHandler(stopDownload))

app.start()
print("Bot started!")
print("Press CTRL+\\ to stop...")
t = Thread(target=downloadRunner)
t.start()
idle()
t.join()
app.stop()
