def hello_world():
    print("hello world")

async def vineet_is_awesome(message,client):
    if message.author == client.user:
        return
    if 'vineet' in message.content:
        await message.channel.send('Vineet is awesome!')