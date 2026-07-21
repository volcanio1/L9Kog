import discord
from discord.ext import commands


class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hi")


async def setup(bot):
    await bot.add_cog(Hi(bot))

