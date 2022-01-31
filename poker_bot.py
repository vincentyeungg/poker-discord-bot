import os
from dotenv import load_dotenv
import discord
from collections import namedtuple

from poker.game import Game, GameState

load_dotenv()
token = os.getenv('BOT_TOKEN')

# setup connection to discord
client = discord.Client()
# dictionary to keep track of games for each channel, allowing only 1 game per channel
live_games = {}

def new_game(game: Game, message: discord.Message):
    # if there are no games created
    if game.state == GameState.NO_GAME:
        game._awaiting_players_to_join()

    return [f"{message.author} has started the game!"]

def show_help(*args):
    # $help command triggered
    commands_help = []
    for command in commands:
        commands_help.append(f"**{command}**: {commands.get(command).description}")
    return commands_help


# contain description of the command, and the respective action
Command = namedtuple("Command", ["description", "action"])

# list of commands users can use to interact with the bot
commands = {
    '$newgame': Command('Starts a new game of Texas Hold\'em poker. Players are start joining now.', new_game),
    '$help': Command('Show the list of available commands.', show_help)
}

# discord bot client handler
@client.event
async def on_ready():
    print(f"Poker bot just logged in as {client.user}")

@client.event
async def on_message(message):
    # this event triggers for every message received, need to ignore messages coming from the bot itself
    if message.author == client.user:
        return

    # if empty message content
    if len(message.content.split()) == 0:
        return

    user_command = message.content.split()[0].lower()

    # not a possible valid command
    if user_command not in commands:
        await message.channel.send(f"'{message.content}' is not a valid command.\nMessage !help to see the list of commands.")
        return

    # based on a command, trigger the specified related function
    # allow only one live game per channel, create a new game object if channel doesn't have ongoing game
    game = live_games.setdefault(message.channel, Game())
    # use message to extract information from users that are entering the command
    bot_response = commands.get(str(user_command)).action(game, message)
    await message.channel.send("\n".join(bot_response))

    return

client.run(token)
