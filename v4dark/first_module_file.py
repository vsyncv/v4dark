def hello_world():
    print("hello world")

async def vineet_is_awesome(message):
    if 'vineet' in message.content:
        await message.channel.send('vineet is awesome!')


async def vineet_is_awesome_checker(message):
    if 'hello' in message.content:
        await message.channel.send('Hello!')