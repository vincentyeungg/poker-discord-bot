import os
from dotenv import load_dotenv
import discord

load_dotenv()
token = os.getenv('BOT_TOKEN')

# _TOKEN = 'OTM1MDE2NjM2NjQwMDA2MjE1.Ye4gGQ.qlk8aY0jpo-4gNzQgc39SFla_x4'

# setup connection to discord
client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # this event triggers for every message received, need to ignore messages coming from the bot itself
    if message.author == client.user:
        return

    # if users enter $hello command, then greet the user
    if message.content.lower() == "$hello":
        await message.channel.send(f"Hello {message.author.name}!")
    elif message.content.lower() == "$bye":
        await message.channel.send(f"Bye {message.author.name}!")

    return


# look to store sensitive keys in a separate file ignored by source control
client.run(token)
