'''
All functions in this file will be in relation to messages.

which isn't the only possible kind, I've noticed.

They all need to be in the on_message() function, or else they won't work.
'''

from v4dark.helper_functions import logger

my_logger = logger(log_filepath='logs/message_related.log', logger_name='message_related') 

async def vineet_is_awesome(message,client):
    if message.author == client.user:
        return
    if 'vineet' in message.content.lower():
        await message.channel.send('Vineet is awesome!')