import os
import discord
import dotenv
from mathbot import commands
from mathbot.keep_alive import keep_alive

# PUBLIC VARIABLES
# ================
# Customize these variables to suit your needs
URL = "https://github.com/hungrybluedev/math-bot/"
VERSION = "0.1.0"
DOCUMENTATION_LINK = "https://github.com/hungrybluedev/math-bot/blob/main/docs.md"
BOT_NAME = "MathBot"
TRIGGER_PREFIX = "$mathbot"

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
            return "%s v%s" % (BOT_NAME, VERSION)
        elif command == "info":
            return "%s v%s; Github: %s" % (BOT_NAME, VERSION, URL)
        else:
            return _DEFAULT_ERROR % (command, DOCUMENTATION_LINK)
    else:
        # 3. Command followed by arguments
        try:
            result = commands.evaluate(command, args[1:])
            if result is not None:
                return "The result is %s" % result
            else:
                return _DEFAULT_ERROR % (command, DOCUMENTATION_LINK)
        except ValueError as err:
            return "%s Link to documentation: %s" % (err, DOCUMENTATION_LINK)


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
        await message.channel.send(_process_command(args))

if __name__ == "__main__":
    # Load the DISCORD_TOKEN environment variable from the .env file if it exists
    dotenv.load_dotenv()
    # Uncomment this line to make sure a web server keeps running
    # keep_alive()
    # Log in to Discord and start processing messages
    _client.run(os.getenv('DISCORD_TOKEN'))
