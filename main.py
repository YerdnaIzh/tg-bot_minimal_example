import os

import pyrogram


bot = pyrogram.Client(
	api_id=os.environ['API_ID'],
	api_hash=os.environ['API_HASH'],
	bot_token=os.environ['BOT_TOKEN'],

	name = ""
)

@bot.on_message()
async def start(client: pyrogram.Client, message: pyrogram.types.Message):
	await message.reply(message.text)

bot.run()