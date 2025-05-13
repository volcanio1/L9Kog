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
        """Move a member through a sequence of voice channels"""
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
        """Move the command user and mentioned user to the nearest empty voice channel"""
        # Check if both users are in voice channels
        if not ctx.author.voice:
            await ctx.send(f"{ctx.author.display_name}, you must be in a voice channel to use this command.")
            return
            
        if not member.voice:
            await ctx.send(f"{member.display_name} is not in a voice channel.")
            return
            
        # Get all voice channels in the guild
        voice_channels = ctx.guild.voice_channels
        
        # Find the nearest empty voice channel (no members in it)
        empty_channels = [channel for channel in voice_channels if len(channel.members) == 0]
        
        if not empty_channels:
            await ctx.send("No empty voice channels available.")
            return
            
        # Find the closest empty channel to either user
        author_channel = ctx.author.voice.channel
        target_channel = None
        
        # If we have empty channels, use the first one
        # A more sophisticated approach could calculate "distance" between channels
        target_channel = empty_channels[0]
        
        # Move both users to the target channel
        await ctx.author.move_to(target_channel)
        await member.move_to(target_channel)
        
        await ctx.send(f"Moved {ctx.author.display_name} and {member.display_name} to {target_channel.name} for privacy.")
    
    @commands.command()
    async def boil(self, ctx, member: discord.Member):
        """Move a member to 'the pot' and play a looping audio"""
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