import discord
from discord.ext import commands
import asyncio


class Move(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def move(self, ctx, member: discord.Member):
        
        if member.voice and member.voice.channel:
            current_channel = member.voice.channel
            voice_channels = [channel for channel in ctx.guild.voice_channels]
            current_index = voice_channels.index(current_channel)

           
            moves = [1, 1, -1, 1, -2]  

           
            for move in moves:
               
                target_index = current_index + move
                if 0 <= target_index < len(voice_channels):
                   
                    await member.move_to(voice_channels[target_index])
                    await asyncio.sleep(0.25)  
                    current_index = target_index
                else:
                    await ctx.send("Could not move further in that direction.")
                    break


async def setup(bot):
    await bot.add_cog(Move(bot))

