#bot.py
import os
import random
from dotenv import load_dotenv #for work with .env files

import discord
from discord.ext import commands
from discord.ext.commands import Bot

#loading token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #reading in the token from .env file
#GUILD = os.getenv('DISCORD_GUILD')

#setting prefix and defining bot
bot = commands.Bot(command_prefix='!')
client = discord.Client() #defining client

#login message
@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected')
	guild = discord.utils.get(bot.guilds)#, name=GUILD)
	print(
		f'The bot is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)

##__Responder__##
#usinig bot.command not bot.event
#giving command name as an argument
#this command is only executed when !command is mentioned, not at each message
#every command must accept alt least one parameter, called context
#a command function is technically called a callback
@bot.command(name='99', help='Responds with a random quoute from brooklyn 99')
async def nine_nine(ctx):
	brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
	response = random.choice(brooklyn_99_quotes)
	await ctx.send(response)


@bot.command(name='kitten', help='Sends a Video of little kittens')
async def nine_nine(ctx):
	brooklyn_99_quotes = [
        'https://www.youtube.com/watch?v=4IP_E7efGWE&t=7',
        'https://youtu.be/xaUUNL3g-mU?t=16',
        (
            'https://www.youtube.com/watch?v=BgIgKcqPd4k'
        ),
    ]
	response = random.choice(brooklyn_99_quotes)
	await ctx.send(response)


#rooling a dice
@bot.command(name='dice', help='Simulates rolling dice.')
#takes the arguments includes a conversion to integers
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
	str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(', '.join(dice))


#create channel
@bot.command(name='create-channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name='generated-voice-channel'):
	guild = ctx.guild
	existing_channel = discord.utils.get(guild.channels, name=channel_name)
	if not existing_channel:
		print(f'Creating a new channel: {channel_name}')
		await guild.create_voice_channel(channel_name)
#error message if user has not right permissions
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
			await ctx.send('You can\'t do that. Pleases ask an Admin')

@bot.command(name='join', pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_channel(channel)


##


bot.run(TOKEN)











