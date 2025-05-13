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