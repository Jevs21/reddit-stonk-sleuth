
import sys
import os
import discord
from dotenv import load_dotenv
load_dotenv()
from reddit.reddit import get_reputation_from_post

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"st0nkbot successfully connected to {len(client.guilds)} server(s).")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'reddit.com/r/' in message.content: # This should be changed to be specific to investing subreddits
        response = await get_reputation_from_post(message.content)
        await message.channel.send(response)


client.run(DISCORD_TOKEN)