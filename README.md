# L9Kog

A Discord bot built with [discord.py](https://discordpy.readthedocs.io/). Its main feature is the `!boil` command, which drags a user into "the pot" voice channel and plays looping boiling water audio.

## Commands

| Command | Description |
| --- | --- |
| `!boil @member` | Moves the mentioned member into a voice channel named **the pot** and plays looping boiling water audio. If the member isn't in a voice channel, the bot reports that instead of moving them. If the audio is already playing in the pot, the bot just says so. |
| `!move @member` | Shuffles the mentioned member through a fixed sequence of voice channels (relative moves: +1, +1, -1, +1, -2), pausing briefly between each hop. Stops early if a move would go out of bounds. |
| `!hi` | Replies with `hi`. |

Any unrecognized command triggers the `!boil` command against whoever typed it, as a fallback/easter egg (see `on_command_error` in `discordbot.py`).

## Requirements

- Python 3.9+
- [FFmpeg](https://ffmpeg.org/) installed and available on your system `PATH` (required by `discord.FFmpegPCMAudio` for audio playback)
- A voice channel named exactly **the pot** in your server (required by `!boil`)
- Python dependencies from `requirements.txt`:
  - `discord.py==2.3.2`
  - `yt-dlp==2023.7.6`
  - `pynacl==1.5.0` (voice support)

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install FFmpeg (e.g. `apt install ffmpeg`, `brew install ffmpeg`, or download from ffmpeg.org) and make sure it's on your `PATH`.
3. Create a Discord application/bot at the [Discord Developer Portal](https://discord.com/developers/applications) and invite it to your server with permissions to view channels, send messages, connect, and speak.
4. Enable the **Server Members**, **Presence**, and **Message Content** privileged intents for your bot in the Developer Portal (the bot requests all three).
5. Set your bot token as an environment variable:
   ```bash
   export DISCORD_BOT_TOKEN=your-token-here
   ```
6. Create a voice channel named **the pot** in your server.
7. Run the bot:
   ```bash
   python discordbot.py
   ```

## Project structure

```
discordbot.py       # Bot entrypoint: sets up intents, loads commands, handles errors
commands/
  boil.py            # !boil - move a member into "the pot" and play boiling water audio
  move.py            # !move - shuffle a member through nearby voice channels
  hi.py              # !hi   - simple ping/reply command
requirements.txt      # Python dependencies
```

Commands are implemented as `discord.py` cogs and loaded dynamically in `load_commands()` in `discordbot.py`.
