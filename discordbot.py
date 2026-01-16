import discord
from discord.ext import commands
import os
import asyncio


TOKEN = os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()
intents.members = True  
intents.presences = True
intents.message_content = True 


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    await load_commands()


async def load_commands():
    """Load all command cogs from the commands directory"""
    command_files = ['hi', 'move', 'boil']
    for command_file in command_files:
        try:
            await bot.load_extension(f'commands.{command_file}')
            print(f'Loaded command: {command_file}')
        except Exception as e:
            print(f'Failed to load command {command_file}: {e}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"!boil {ctx.author.mention}")  
        member = ctx.author  
        await ctx.invoke(bot.get_command('boil'), member=member)  


if __name__ == '__main__':
    bot.run(TOKEN)
