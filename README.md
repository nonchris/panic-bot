# panic-bot

This bot is a litte fun project I started while beeing at home. 
It was originally meant for a server/guild where me and some friends hang out and learned together.  

### What does panic do?
panic checks a voice-channel namend 'panicroom'.  
When somebody joins that channel panic will send a notification message telling the other members that one of their friends ins panicing. This happens in a text-channel called 'emergency'.  
In addition to that he sends a link to a cat-video from youtube. (Those Videos are hardcoded in the bot).  
There are also some messaged when more people join the 'panicroom'.  
I also included a comment `!cat` to get an other video from that list.  
There are some other minor functions like rolling a dice or getting a quote from brooklyn99 (some people will now know where I started coding that bot ^^)  

### Notice
The bot is coded in english, means that all comments and variables have english names.  
The specified messasges the bot posts in random orders are in german.  

### Setup
You need a discord-API token, the bot.py file and a file named `config.py` including your token (just rename the `dummy-config.py`).  
Both files need to be in the same directory.  

### Version
This Bot is created using python 3.8.3 and the discord.py library from early 2020.