#bot.py
import os
import random
from dotenv import load_dotenv #for work with .env files (credentials)
import config #for server configs

import discord
from discord.ext import commands
from discord.ext.commands import Bot

#loading token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #reading in the token from .env file
#GUILD = os.getenv('DISCORD_GUILD')

server_channels = {} # Server channel cache

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
		f'{guild.name} (id: {guild.id})'
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
##Not working
# @bot.command(name='join', pass_context=True)
# async def join(ctx):
# 	channel = ctx.message.author.voice.voice_channel
# 	await client.join_channel(channel)


### CHECK FOR CHANNEL JOIN ###

def find_channel(server, refresh = False):
    """
    Find and return the channel to log the voice events to.
    
    :param server: The server to find the channel for.
    :param refresh: Whether to refresh the channel cache for this server.
    """
    if not refresh and server in server_channels:
        return server_channels[server]
        
    for channel in client.get_all_channels():
        if channel.server == server and channel.name == config.CHANNEL_NAME:
            print("%s: refreshed destination log channel" % server)
            server_channels[server] = channel
            return channel
            
    return None



@bot.event
async def on_voice_state_update(member, before, after):
    #if before.channel is None and after.channel is not None:
    if after.channel.id == 712247842995175426:
        #print("there is something")
        print(after.channel)
        #print(member.guild.system_channel)
        print("panic!!!")
        await member.guild.system_channel.send("Alarm!")
            

# @client.event
# async def on_voice_state_update(member_before, member_after):
#     """
#     Called when the voice state of a member on a server changes.
    
#     :param member_before: The state of the member before the change.
#     :param member_after: The state of the member after the change.
#     """
#     server = member_after.server
#     channel = find_channel(server)
    
#     voice_channel_before = member_before.voice_channel
#     voice_channel_after = member_after.voice_channel
    
#     print("something happend")
#     if voice_channel_before == voice_channel_after:
#         # No change
#         return
    
#     if voice_channel_before == None:
#         # The member was not on a voice channel before the change
#         msg = "%s joined voice channel _%s_" % (member_after.mention, voice_channel_after.name)
#     else:
#         # The member was on a voice channel before the change
#         if voice_channel_after == None:
#             # The member is no longer on a voice channel after the change
#             msg = "%s left voice channel _%s_" % (member_after.mention, voice_channel_before.name)
#         else:
#             # The member is still on a voice channel after the change
#             msg = "%s switched from voice channel _%s_ to _%s_" % (member_after.mention, voice_channel_before.name, voice_channel_after.name)
    
#     # Try to log the voice event to the channel
#     try:
#         await client.send_message(channel, msg)
#     except:
#         # No message could be sent to the channel; force refresh the channel cache and try again
#         channel = find_channel(server, refresh = True)
#         if channel == None:
#             # The channel could not be found
#             print("Error: channel #%s does not exist on server %s." % (config.CHANNEL_NAME, server))
#         else:
#             # Try sending a message again
#             try:
#                 await client.send_message(channel, msg)
#             except discord.DiscordException as exception:
#                 # Print the exception
#                 print("Error: no message could be sent to channel #%s on server %s. Exception: %s" % (config.CHANNEL_NAME, server, exception))


bot.run(TOKEN)











