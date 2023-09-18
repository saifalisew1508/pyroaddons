from pyrogram import Client

from pyroaddons import patch  # type : ignore

app = Client(
    ":pyroaddons",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

app.start()
