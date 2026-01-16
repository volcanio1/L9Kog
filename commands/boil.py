import discord
from discord.ext import commands
import yt_dlp


class Boil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.youtube_url = 'https://www.youtube.com/watch?v=VaVtu9L7wfc'
        self.ytdlp_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'default_search': 'ytsearch',
            'source_address': '0.0.0.0'  
        }

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
           
            with yt_dlp.YoutubeDL(self.ytdlp_opts) as ydl:
                info = ydl.extract_info(self.youtube_url, download=False)
                audio_url = info['url']
            vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)

        
        with yt_dlp.YoutubeDL(self.ytdlp_opts) as ydl:
            info = ydl.extract_info(self.youtube_url, download=False)
            audio_url = info['url']
        vc.play(discord.FFmpegPCMAudio(audio_url), after=repeat_audio)


async def setup(bot):
    await bot.add_cog(Boil(bot))

