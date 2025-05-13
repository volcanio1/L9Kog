import discord
from discord.ext import commands
import asyncio
from config import TOKEN

async def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    await bot.load_extension("cogs.general_commands")
    await bot.load_extension("cogs.voice_commands")
    await bot.load_extension("cogs.events")
    
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main()) 