import os

# Bot Configuration
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# YouTube Configuration
YOUTUBE_URL = 'https://www.youtube.com/watch?v=VaVtu9L7wfc'
YTDLP_OPTS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0'  
}

# FFmpeg Configuration for Replit
FFMPEG_OPTIONS = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
} 