import discord
import config
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
description="Hello world"

client = commands.Bot(command_prefix='?', description=description,intents=intents)

async def load_cogs():
    try:
        await client.load_extension("cog.general")
    except Exception as e:
        print(f"Failed to load cog.general: {e}")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def hello(message):
    await message.channel.send('Hello from the bot')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

async def main():
    await load_cogs()
    await client.start(config.TOKEN)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bot stopped.")