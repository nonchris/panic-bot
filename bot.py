import os

import discord #imports the discord.py library
from dotenv import load_dotenv #for work with .env files

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #reading in the token from .env file

client = discord.Client() #defining client

#event handler, which handles events, when client established connection to discord
#and has finished preparing the data from Discord
#Short: What happens when client is ready for further actions
@client.event
async def on_ready(): 
	print(f'{client.user} has connected to Discord')

client.run(TOKEN)
