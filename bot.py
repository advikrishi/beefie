import discord

TOKEN = 'NTEzMjY3MzI2NjgzMDU0MDgw.DtlZAw.Qny63gZn2w7cpo1RSc8YuriEzy8'

client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('!hellos'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
		
	elif message.content.startswith('!qna'):
		msg2 = "This is one hell of a qna"
		await client.send_message(message.channel, msg2)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run('TOKEN')
