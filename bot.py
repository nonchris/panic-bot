#bot.py
import os
import random
from dotenv import load_dotenv #for work with .env files (credentials)

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

game = discord.Game('Watches Panicroom')
#login message
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected')
    guild = discord.utils.get(bot.guilds)#, name=GUILD)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Katzenvideos"))
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



cat_videos = [
                'https://www.youtube.com/watch?v=4IP_E7efGWE&t=7',
                'https://youtu.be/xaUUNL3g-mU?t=16',
                (
                'https://www.youtube.com/watch?v=BgIgKcqPd4k'
                ),
                'https://youtu.be/XyNlqQId-nk?t=12',
                'https://youtu.be/tpiyEe_CqB4?t=28',
                'https://youtu.be/uHKfrz65KSU',
                'https://youtu.be/-8JQB_wXjmk?t=11'
            ]

#Cat Trigger
@bot.command(name='cat', help='Sends a Video of little kittens')
async def nine_nine(ctx):
    response = random.choice(cat_videos)
    await ctx.send(response)

panic_member = None #Var to store the user that paniced
voice_members = 0 #Number of people in voice, needed for compares later
# Panic Room
@bot.event
async def on_voice_state_update(member, before, after):

    #Defining stings for messages
    panic_alert = [
                ':rotating_light: ARLARM! %s ist im Panicroom! :rotating_light: ',
                ':rotating_light: Code RED, ich wiederhole **Code RED**! %s ist im Panicroom! :rotating_light: ',
            ]


    wait_message = [
                'Hier schonmal etwas Aufheiterndes, bis wirkliche Hilfe eintrifft',
                'Ok - Jetzt bloß nicht durchdrehen, hier ist etwas Ablenkung',
                'Ich kann dir keinen Alkohol anbieten - Das hier wird auch helfen'
            ]
   

    panic_empty = [
                'Der Panicroom ist wieder leer! - Ist die Lage gebannt? :smiley: ',
                'Alle haben den Panicroom verlassen, hoffentlich ist keiner gestorben :grimacing:',
                'Diese Ruhe - Sind alle Existenzkrisen überwunden? :thinking:'

            ]

    first_aid = [
                ', halte durch! Rettung naht! :fire_engine:',
                ', Unterstützung ist auf dem Weg! - Oder will da jemand nur mit dir weinen?',
                ', jemand interessiert sich für dich und deine Sorgen! Moment? War der Join ein versehen? :thinking:',
                ', du hast Freunde! Geteiltes Leid ist doppelt... eh ne, ich meine halbes Leid'


            ]

    more_aid = [
                'Noch mehr Menschen im Panicroom? Sollte man jetzt Panik bekommen? :scream:',
                'Mehr Leute gleich mehr Pani-, eh... Trost meine ich! (*hust*)',
                (
                    'War jetzt schon der Gruppentherapie-Termin?!\n '
                    'Wartet! Ich hole nur noch schnell meinen Kaffe! :coffee:  '
                )
            ]

    #setting output channels
    notify_channel = 713457148688072744
    panic_channel = 712247842995175426
    
    #getting global members count from previous run of that function
    global voice_members

    #check if really someone joined/left the channel or if only someone muted himself
    #by comparing number of users in channel
    #two options wether user joined or left panicroom
    #retutns if members in channel stayed the same
    #if before is panicroom:
    if before.channel == None: #check for member that just joined voice
        None
    elif before.channel.id == panic_channel:
        if len(before.channel.members) == voice_members:
            return
    else:
        None

    #if after is panicroom:
    if after.channel == None: #check for member that left voice
        None  
    elif after.channel.id == panic_channel:
        if len(after.channel.members) == voice_members:
            return
    else:
        None


    ## No Panic
    #triggered if channel becomes empty again
    if before.channel == None: #check for member that just joined voice
        None

    #if channel empty
    elif before.channel.id == panic_channel:
        if len(before.channel.members) == 0: #when panic channel becomes empty again
            channel = bot.get_channel(notify_channel)

            #message:
            await channel.send(random.choice(panic_empty))
        #if panic member is alone again
        #elif len(before.channel.members) == 1:


    ####_PANIC_####
    if after.channel == None: #check for member that left voice
        None   
    elif after.channel.id == panic_channel: #main panic function
            
        if len(after.channel.members) == 1: #when first user joins voice
            global panic_member #import global Var 
            panic_member = member.mention #write/save global var
            
            #Panic Alert!
            channel = bot.get_channel(notify_channel)
            await channel.send(random.choice(panic_alert) % member.mention)
            #Cat Video / Message
            await channel.send(random.choice(wait_message)+ ': ' + random.choice(cat_videos))

                #await member.guild.channel.send("Alarm!")

        #Second member / first aid person
        elif len(after.channel.members) == 2:
                
            #message for first aid
            #mentioning also panic member
            channel = bot.get_channel(notify_channel)
            await channel.send(panic_member + random.choice(first_aid))

        #More aid! 3rd user and more
        elif len(after.channel.members) > 2:
            channel = bot.get_channel(notify_channel)
            await channel.send(random.choice(more_aid))

    #getting amount of members in channel
    #saving it for later iterations as a comparable value
    if before.channel == None: #check for member that just joined voice
        None
    elif before.channel.id == panic_channel:
        voice_members = len(before.channel.members)
    elif after.channel.id == panic_channel:
        voice_members = len(after.channel.members)


bot.run(TOKEN)











