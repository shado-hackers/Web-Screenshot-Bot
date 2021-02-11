from pyrogram import Client
from creds import my

plugins = dict(root="plugins")
app = Client(
    "Webshot Bot",
    bot_token=my.BOT_TOKEN,
    api_id=my.API_ID,
    api_hash=my.API_HASH,
    update_channel=my.UPDATE_CHANNEL
    plugins=plugins,
)

app.run()
