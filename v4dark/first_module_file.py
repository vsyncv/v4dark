'''

Discord module documentation:

https://discordpy.readthedocs.io/en/latest/api.html
'''
from dotenv import load_dotenv
import os
import discord
from v4dark.message_related import vineet_is_awesome,get_stock_price

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Yep... So now you better have that .env file, or else this will break.

client = discord.Client()

@client.event
async def on_ready(): # These names aren't random. You have to name them properly. see url below (which you normally don't have to do, that's a discord module thing).
    '''
    https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready
    '''
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return # ignore yourself.
    
    await vineet_is_awesome(message)
    await get_stock_price(message)

def start_bot():
    client.run(TOKEN)