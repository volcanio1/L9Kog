import discord
from discord.ext import commands
import yt_dlp
import asyncio
from config import YOUTUBE_URL, YTDLP_OPTS

class VoiceCommands(commands.Cog):
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
    
    @commands.command()
    async def priv(self, ctx, member: discord.Member):
        if not ctx.author.voice:
            await ctx.send(f"{ctx.author.display_name}, you must be in a voice channel to use this command.")
            return
            
        if not member.voice:
            await ctx.send(f"{member.display_name} is not in a voice channel.")
            return
            
        voice_channels = ctx.guild.voice_channels
        empty_channels = [channel for channel in voice_channels if len(channel.members) == 0]
        
        if not empty_channels:
            await ctx.send("No empty voice channels available.")
            return

        target_channel = None
        
        target_channel = empty_channels[0]
        
        await ctx.author.move_to(target_channel)
        await member.move_to(target_channel)
        
        await ctx.send(f"Moved {ctx.author.display_name} and {member.display_name} to {target_channel.name} for privacy.")
    
    @commands.command()
    async def boil(self, ctx, member: discord.Member):
        pot_channel = discord.utils.get(ctx.guild.voice_channels, name="the pot")
        if not pot_channel:
            await ctx.send("The 'the pot' channel does not exist.")
            return

        if member.voice:
            await member.move_to(pot_channel)
        else:
            await ctx.send(f"{member.display_name} is not in a voice channel.")
            return

        if not ctx.voice_client:
            vc = await pot_channel.connect()
        else:
            vc = ctx.voice_client
            await vc.move_to(pot_channel)

        if vc.is_playing():
            await ctx.send("Audio is already playing in 'the pot'.")
            return

        def repeat_audio(error):
            if error:
                print(f"Error occurred: {error}")
            with yt_dlp.YoutubeDL(YTDLP_OPTS) as ydl:
                info = ydl.extract_info(YOUTUBE_URL, download=False)
                audio_url = info['url']
            vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)

        with yt_dlp.YoutubeDL(YTDLP_OPTS) as ydl:
            info = ydl.extract_info(YOUTUBE_URL, download=False)
            audio_url = info['url']
        vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)

async def setup(bot):
    await bot.add_cog(VoiceCommands(bot)) 