import discord
from discord.ext import commands
import yt_dlp
import asyncio
import random
import os

YOUTUBE_URL = 'https://www.youtube.com/watch?v=VaVtu9L7wfc'
# Ensure FFmpeg is correctly set up
ytdlp_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0'  # Bind to IPv4 for improved compatibility
}

# Replace 'YOUR_BOT_TOKEN' with your bot's actual token
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intents are necessary to allow the bot to access certain information
intents = discord.Intents.default()
intents.members = True  # Ensure this is enabled to interact with members
intents.presences = True
intents.message_content = True 

# Set up the bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def hi(ctx):
    await ctx.send("hi")

@bot.command()
async def move(ctx, member: discord.Member):
    # Check if the member is in a voice channel
    if member.voice and member.voice.channel:
        current_channel = member.voice.channel
        voice_channels = [channel for channel in ctx.guild.voice_channels]
        current_index = voice_channels.index(current_channel)

        # Define the moves (down, down, up, down, back to start)
        moves = [1, 1, -1, 1, -2]  # -3 is for returning to the original channel

        # Execute each move with a 0.5-second delay
        for move in moves:
            # Calculate the target channel index
            target_index = current_index + move
            if 0 <= target_index < len(voice_channels):
                # Move the member to the target channel
                await member.move_to(voice_channels[target_index])
                await asyncio.sleep(0.25)  # Wait 0.5 seconds between moves
                current_index = target_index
            else:
                await ctx.send("Could not move further in that direction.")
                break
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"!boil {ctx.author.mention}")  # Outputs "!boil" with a mention of the original sender
        member = ctx.author  # Treats the original sender as the member for the boil command
        await ctx.invoke(bot.get_command('boil'), member=member)  # Invokes the boil command directly


@bot.command()
async def boil(ctx, member: discord.Member):
    # Find the "the pot" channel
    pot_channel = discord.utils.get(ctx.guild.voice_channels, name="the pot")
    if not pot_channel:
        await ctx.send("The 'the pot' channel does not exist.")
        return

    # Move the member to "the pot" channel
    if member.voice:
        await member.move_to(pot_channel)
    else:
        await ctx.send(f"{member.display_name} is not in a voice channel.")
        return

    # Bot joins "the pot" channel
    if not ctx.voice_client:
        vc = await pot_channel.connect()
    else:
        vc = ctx.voice_client
        await vc.move_to(pot_channel)

    # Check if already playing, to avoid restarting the audio
    if vc.is_playing():
        await ctx.send("Audio is already playing in 'the pot'.")
        return

    # Function to loop the audio
    def repeat_audio(error):
        if error:
            print(f"Error occurred: {error}")
        # Re-extract audio URL and play again for looping
        with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
            info = ydl.extract_info(YOUTUBE_URL, download=False)
            audio_url = info['url']
        vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)

    # Start playing and looping the audio
    with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
        info = ydl.extract_info(YOUTUBE_URL, download=False)
        audio_url = info['url']
    vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)


bot.run(TOKEN)
