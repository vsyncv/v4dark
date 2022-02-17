def hello_world():
    print("hello world")

async def vineet_is_awesome(message):
    if 'vineet' in message.content:
        await message.channel.send('Vineet is awesome!')