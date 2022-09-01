import discord
from discord.ext import commands
from env import DISCORD_TOKEN #created another file called 'env' and put the token in "DISCORD_TOKEN=('')"  within that file
TOKEN = (DISCORD_TOKEN)

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

#on_ready() event handler, which handles the event when the Client has established a connection to Discord and it has finished preparing the data that Discord has sent, such as login state, guild and channel data, and more.
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


#on_message() occurs when a message is posted in a channel that your bot has access to.
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith(message.content):
         await message.channel.send('Hello') 


client.run(TOKEN)