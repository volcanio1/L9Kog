import discord
from discord.ext import commands
import asyncio
from config import TOKEN

async def main():
    # Set up intents
    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.message_content = True

    # Initialize bot
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    # Load cogs
    await bot.load_extension("cogs.general_commands")
    await bot.load_extension("cogs.voice_commands")
    await bot.load_extension("cogs.events")
    
    # Run the bot
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main()) 