import pyrogram
from pyrogram.filters import reply

import config

bot = pyrogram.Client(
	api_id=config.API_ID,
	api_hash=config.API_HASH,
	bot_token=config.BOT_TOKEN,

	name = ""
)

@bot.on_message()
async def start(client: pyrogram.Client, message: pyrogram.types.Message):
	await message.reply(message.text)

bot.run()