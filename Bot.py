'''

Discord module documentation:

https://discordpy.readthedocs.io/en/latest/api.html
'''
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from v4dark.message_related import vineet_is_awesome,get_stock_price
from v4dark.helper_functions import logger

my_logger = logger(log_filepath='logs/first_module_file.log', logger_name='first_module_file')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Yep... So now you better have that .env file, or else this will break.

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready(): # These names aren't random. You have to name them properly. see url below (which you normally don't have to do, that's a discord module thing).
    '''
    https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready
    '''
    my_logger.info('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return # ignore yourself.
    
    await vineet_is_awesome(message)
    await get_stock_price(message)

def start_bot():
    client.run(TOKEN)
    