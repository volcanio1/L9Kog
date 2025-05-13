# Discord Bot

A Discord bot with voice channel manipulation and audio features.

## Structure
- `main.py` - Entry point for the bot
- `config.py` - Configuration settings
- `cogs/` - Command and event modules
  - `general_commands.py` - Basic commands
  - `voice_commands.py` - Voice channel commands
  - `events.py` - Event handlers


### Prerequisites
- Python 3.8 or higher


### Step 1: Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Navigate to the "Bot" tab and click "Add Bot"
4. Under the "TOKEN" section, click "Copy" to copy your bot token
5. Keep this token secure! You'll need it in Step 4

### Step 2: Install Dependencies
```bash
# For Windows
pip install -r requirements.txt

# For Linux/macOS
pip3 install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a file named `.env` in the main directory:
```bash
# Create and open .env file
# For Windows
notepad .env

# For Linux/macOS
nano .env
```

Add your Discord bot token to the env file:
```
DISCORD_BOT_TOKEN=your_bot_token_here
```
Save and close the file.

### Step 4: Invite the Bot to Your Server
1. Go back to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application and go to the "OAuth2" tab
3. Under "OAuth2 URL Generator", select "bot" under the "SCOPES" section
4. Under "BOT PERMISSIONS", select:
   - "Read Messages/View Channels"
   - "Send Messages"
   - "Connect" (to voice channels)
   - "Speak" (in voice channels)
   - "Move Members" (for voice channel commands)
5. Copy the generated URL and open it in your browser
6. Select the server you want to add the bot to and confirm

### Step 5: Run the Bot
```bash
# For Windows
python main.py

# For Linux/macOS
python3 main.py
```

## Available Commands
- `!hi` - Simple greeting command
- `!move @user` - Move a mentioned user through a sequence of voice channels
- `!boil @user` - Move a mentioned user to "the pot" channel and play audio
- `!priv @user` - Move both you and the mentioned user to a private empty voice channel

## Requirements
- Make sure you have a voice channel named "the pot" for the `!boil` command
- The bot needs proper permissions to move users between voice channels
