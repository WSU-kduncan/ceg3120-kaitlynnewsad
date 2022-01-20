
import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    office_quotes = [
        'What kind of bear is best?'
        (
            
'Thats a ridculous question. Its debatable. There are basically two schools of thought--'

        ),
    ]

    _quote = [
        'Hi. Im great. How are you.',
    ]

    if message.content == 'Hello! How are you.':
        #response = random.choice(office_quotes)
        response = random.choice(_quote)
        await message.channel.send(response)

client.run(TOKEN)
