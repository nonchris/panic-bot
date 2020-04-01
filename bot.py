import os

import discord #imports the discord.py library
from dotenv import load_dotenv #for work with .env files

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #reading in the token from .env file
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client() #defining client

#event handler, which handles events, when client established connection to discord
#and has finished preparing the data from Discord
#Short: What happens when client is ready for further actions
#Will be callled once when bot connected
@client.event
async def on_ready(): 
	for guild in client.guilds: #loop though guild data to find the required server
		if guild.name == GUILD:
			break


	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)

	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

client.run(TOKEN)
