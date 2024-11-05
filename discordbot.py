import discord
from discord.ext import commands
import yt_dlp
import asyncio
import random
import os

YOUTUBE_URL = 'https://www.youtube.com/watch?v=VaVtu9L7wfc'

ytdlp_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0'  
}


TOKEN = os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()
intents.members = True  
intents.presences = True
intents.message_content = True 


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def hi(ctx):
    await ctx.send("hi")

@bot.command()
async def move(ctx, member: discord.Member):
    
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
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"!boil {ctx.author.mention}")  
        member = ctx.author  
        await ctx.invoke(bot.get_command('boil'), member=member)  


@bot.command()
async def boil(ctx, member: discord.Member):
    
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
       
        with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
            info = ydl.extract_info(YOUTUBE_URL, download=False)
            audio_url = info['url']
        vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)

    
    with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
        info = ydl.extract_info(YOUTUBE_URL, download=False)
        audio_url = info['url']
    vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)


bot.run(TOKEN)
