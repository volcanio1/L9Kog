import discord
from discord.ext import commands
import asyncio
from config import TOKEN
from flask import Flask
from threading import Thread

# Flask web server for keeping the bot alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    server = Thread(target=run_flask)
    server.daemon = True
    server.start()

async def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    await bot.load_extension("cogs.general_commands")
    await bot.load_extension("cogs.voice_commands")
    await bot.load_extension("cogs.events")
    
    await bot.start(TOKEN)

if __name__ == "__main__":
    keep_alive()  # Start the web server
    asyncio.run(main()) 