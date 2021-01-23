<div align=center style="margin: 0 auto;">
<img src="logo.png" width="400px" style="width: 400px;">
</div>

# Introduction



# Usage

The source code for this bot is freely available under the [MIT License](#license). Anyone can clone this repository and host their own instance of this bot.

Refer to the [documentation](docs.md) for all the supported commands and the syntax.

In case you find a bug, or notice that a certain feature is absent but want it to be added, consider looking at the [existing issues](https://github.com/hungrybluedev/math-bot/issues). If nothing matches what you found, [create a new Issue](https://github.com/hungrybluedev/math-bot/issues/new/choose).

# Instructions for Local Setup

This section contains instructions that can be followed by users to have their own instance of this bot running either on their local machine. These can be adapted fairly easily and users can host their bots online on services like [Repl.it](https://repl.it/) and [Heroku](https://www.heroku.com/).

## Prerequisites

### Install Git and Python

1. Install Python 3.8 or higher and make sure it is added to path.
2. Install Git, add it to path and configure the username and email.

A Github account is optional, but you will need it if you want to contribute code to this repository. Make sure you use the same email as in step 2.

### Obtain the Source Code

1. Navigate to a directory where you want to store the project.
2. Type `git clone https://github.com/hungrybluedev/math-bot.git`
3. Enter the newly created directory using `cd math-bot`

### Obtain Discord Token

Follow the relevant sections of [this tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) by **FreeCodeCamp** to obtain the required token.

> ⚠️ **WARNING:** Do not share this token with anyone else, especially online. Do not add it to a repository. If you have done so accidentally, you should regenerate the token immediately.

### Prepare `.env` File

1. Create a **new file** with the name `.env` in the [mathbot](mathbot) directory. This directory also contains files like [main.py](mathbot/main.py), [commands.py](mathbot/commands.py), and so on.
2. Type `DISCORD_TOKEN=` and then paste the Discord Bot token generated in the previous step. Do not add spaces around the `=`.
3. Ensure that this file does not appear when you type `git status` in the terminal. If it does, add `.env` in a new line in the file [.gitignore](.gitignore)

## Commands

### Starting the Bot

Navigate to the root of the project and execute:

```bash
python -m mathbot.main
```

The bot will log in and block inputs. In order to exit the main loop, press <kbd>Ctrl</kbd>+<kbd>C</kbd>

### Running the Unit Tests

In the root directory, execute:

```bash
python -m unittest mathbot.test
```

This will execute all the tests present in [mathbot.test.py](mathbot/test.py)

# Hosting an Instance

Generally, users might prefer hosting an instance of this bot (for free) rather than self-hosting it on their machines. Two approaches are recommended:

1. Using [Repl.it](https://repl.it/) - Users can follow this [excellent tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) by **FreeCodeCamp** to learn how to host an instance of this bot for free.
2. Using [Heroku](https://www.heroku.com/) - Another approach that might need a bit more configuration than the previous one: following [this tutorial](https://www.techwithtim.net/tutorials/discord-py/hosting-a-discord-bot-for-free/) by Tech with Tim.

# License

This project is licensed under the [MIT License](LICENSE).

# Support

If this project has been useful to you, please consider supporting me on Ko-fi or Patreon.

[<img style="height: 36px;" height="36" src="https://raw.githubusercontent.com/hungrybluedev/hungrybluedev/master/kofi.webp">](https://ko-fi.com/hungrybluedev)
[<img style="height: 36px;" height="36"  src="https://raw.githubusercontent.com/hungrybluedev/hungrybluedev/master/patreon.webp">](https://www.patreon.com/hungrybluedev)
