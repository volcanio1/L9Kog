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
    'source_address': '0.0.0.0',
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'logtostderr': False,
    'geo_bypass': True,
    'geo_bypass_country': 'US',
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-us,en;q=0.5',
        'Sec-Fetch-Mode': 'navigate',
    }
}

# Alternative audio URL (used only for reference, not actively used)
ALTERNATIVE_AUDIO_URL = ""

# FFmpeg Configuration for Replit
FFMPEG_OPTIONS = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
} 