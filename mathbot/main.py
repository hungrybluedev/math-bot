import os
import discord
import dotenv
from mathbot import commands
from mathbot.keep_alive import keep_alive

# PUBLIC VARIABLES
# ================
# Customize these variables to suit your needs
URL = "https://github.com/hungrybluedev/math-bot/"
DOCUMENTATION_LINK = "<https://github.com/hungrybluedev/math-bot/blob/main/docs.md>"
BOT_NAME = "MathBot"
TRIGGER_PREFIX = "$mathbot"
# This combination of COMPACT_FORMAT and GENERATOR_LIMIT keeps the character
# count under 2000. This prevents errors returned by Discord's API. Therefore,
# BE CAREFUL WHILE CHANGING THESE VALUES; EXPERIMENT LOCALLY BEFORE DEPLOYMENT
COMPACT_FORMAT = "%.4f"
GENERATOR_LIMIT = 250
# Try to obtain the version from git, otherwise retain default
VERSION = "v0.1"
try:
    import subprocess
    cmd = "git describe".split()
    VERSION = subprocess.check_output(cmd).decode().strip()
except:
    pass

# PRIVATE VARIABLES
# =================
_client = discord.Client()
_DEFAULT_ERROR = "Could not process the command: %s. Please refer to the documentation: %s"


def _process_command(args):
    """
    Returns a string containing the result of executing the command with the arguments given.
    """
    n = len(args)
    if n == 0:
        # 1. When nothing is provided
        return "No commands given. Please refer to the documentation: %s" % DOCUMENTATION_LINK

    command = args[0].lower()
    if n == 1:
        # 2. Single word commands
        if command == "hello" or command == "help":
            return "Hello, I'm %s! I can evaluate some common math functions. Read the documentation to know more: %s" % (BOT_NAME, DOCUMENTATION_LINK)
        elif command == "version":
            return "%s %s" % (BOT_NAME, VERSION)
        elif command == "info":
            return "%s %s; Github: %s" % (BOT_NAME, VERSION, URL)
        else:
            result = commands.evaluate(command, [])
            if result is not None:
                return result
            else:
                return _DEFAULT_ERROR % (command, DOCUMENTATION_LINK)
    else:
        # 3. Command followed by arguments
        try:
            result = commands.evaluate(command, args[1:])
            if result is not None:
                return result
            else:
                return _DEFAULT_ERROR % (command, DOCUMENTATION_LINK)
        except ValueError as err:
            return "%s Link to documentation: %s" % (err, DOCUMENTATION_LINK)
        except:
            return "We've encountered an unexpected error. Please create a new issue at %sissues" % URL


@_client.event
async def on_ready():
    print("We have logged in as %s" % _client.user)


@_client.event
async def on_message(message):
    if message.author == _client.user:
        # Do not respond to messages from yourself
        return

    if message.content.startswith(TRIGGER_PREFIX):
        args = message.content[len(TRIGGER_PREFIX):].strip().split()
        await message.reply(_process_command(args))

if __name__ == "__main__":
    # Load the DISCORD_TOKEN environment variable from the .env file if it exists
    dotenv.load_dotenv()
    # Uncomment this line to make sure a web server keeps running
    # keep_alive()
    token = os.getenv('DISCORD_TOKEN')
    if token is not None:
        # Log in to Discord and start processing messages
        _client.run(token)
    else:
        print("Could not obtain the token. Please obtain a Discord Bot token and place it in the .env file. Follow the instructions in the README: %s" % URL)
