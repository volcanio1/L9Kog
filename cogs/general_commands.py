import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hi(self, ctx):
        """Simple greeting command"""
        await ctx.send("hi")

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot)) 