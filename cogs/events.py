import discord
from discord.ext import commands

class EventHandlers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Event triggered when the bot is ready"""
        print(f'{self.bot.user} has connected to Discord!')
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handle command errors"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"!boil {ctx.author.mention}")
            member = ctx.author
            await ctx.invoke(self.bot.get_command('boil'), member=member)

async def setup(bot):
    await bot.add_cog(EventHandlers(bot)) 