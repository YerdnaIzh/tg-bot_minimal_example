import pyrogram


bot = pyrogram.Client(
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN,

	name = ""
)

@bot.on_message()
async def start(client: pyrogram.Client, message: pyrogram.types.Message):
	await message.reply(message.text)

bot.run()