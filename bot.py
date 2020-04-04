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
#client handles the event that Client has made a connection
@client.event
#on_ready defines when thsi function is set.
#name has to be like this, this is not the choice of the autor
async def on_ready(): 
	# #lambda function that seaches for the name of GUILD - an other expression for a for-search
	# #Resturns if server is not found: AttributeError: 'NoneType' object has no attribute 'name'
	# #lambda function stops when result found, like "break"
	# guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
	# print(
	# 	f'{client.user} is connected to the following guild:\n'
	# 	f'{guild.name}(id: {guild.id})'
	# )

	#finds specified Server in all guilds the client is on and gives information as output
	#only returns element if all atributes of that iterable element are satisfied
	guild = discord.utils.get(client.guilds, name=GUILD)
	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)

	#A fucntion that lists all members of the guild set in guild.name
	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to Hell!'
		)
	print(f'{member.name} ({member.id}) joined')

client.run(TOKEN)