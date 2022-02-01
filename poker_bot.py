import os
from dotenv import load_dotenv
import time
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
        # the player that joins the game automatically enters the game
        game.add_player(message.author)
        # change the state of the game to waiting for players
        game._awaiting_players_to_join()

        messages = [f"{message.author} has started a new game!", "Message $join to join the game."]

        # remove this line, only for testing use
        print(game.players)

        return messages

    else:
        # if a game is already created, a game could already be happening, or a player might have wanted to join instead
        messages = [f"A game has already been started."]
        if game.state == GameState.WAITING_FOR_PLAYERS:
            # inform the user to use $join instead
            messages.append(f"You can still join the game. Message $join to join that game.")

        return messages

def join_game(game: Game, message: discord.Message):
    # ensure there is a game begun, and in current stage of waiting for players
    if game.state == GameState.NO_GAME:
        return ["No game has been started yet. Message $newgame to create a new game."]
    elif game.state != GameState.WAITING_FOR_PLAYERS:
        return [f"The game is currently in process, {message.author}. You cannot join right now."]
    elif game.add_player(message.author):
        # if new player is joining
        return [f"{message.author} has joined the game. ", "Message $join to join the game."]
    else:
        return [f"You already joined the game {message.author}."]

def start_game(game: Game, message: discord.Message):
    # once players are confirmed, start the game
    if game.state == GameState.NO_GAME:
        return ["Message $newgame to start a new game."]
    elif game.state != GameState.WAITING_FOR_PLAYERS:
        return [f"The game has already started, {message.author}. ", "Please wait for the current game to finish first."]
    elif not game.is_player_in_game(message.author):
        return [f"You are not part of the game yet, {message.author}. ", "Please message $join if you want to play."]
    elif len(game.players) < 2:
        return [f"The game must have at least 2 players to begin."]
    else:
        game.start_game()
        return [f"Game is starting now..."]

def play_game(game: Game, message: discord.Message):
    if game.state == GameState.NO_GAME:
        return ["Message $newgame to start a new game."]
    elif game.state == GameState.WAITING_FOR_INITIAL_CARDS_TO_BE_DEALT:
        # can begin the fast version of the game (no bets or fold)
        messages = []
        messages.append("\nInitial round starting now...")
        game.hand_out_initial_two_cards_to_players()
        messages.append(f"Everyone's hands after dealing initial 2 cards: ")
        for player_name, player_cards in game.get_cards_of_all_players().items():
            messages.append(f"{player_name}'s cards are: {player_cards}")

        # flop round
        messages.append("\nFlop round beginning now...")
        game.hand_out_three_community_cards_to_all_players()
        messages.append(f"Everyone's cards after the flop round: ")
        for player_name, player_cards in game.get_cards_of_all_players().items():
            messages.append(f"{player_name}'s cards are: {player_cards}")

        # turn round
        messages.append("\nTurn round beginning now...")
        game.hand_out_turn_card_to_all_players()
        messages.append(f"Everyone's cards after the turn round are:")
        for player_name, player_cards in game.get_cards_of_all_players().items():
            messages.append(f"{player_name}'s cards are: {player_cards}")

        # river round
        messages.append("\nRiver round beginning now...")
        game.hand_out_river_card_to_all_players()
        messages.append(f"Everyone's cards after the river round are: ")
        for player_name, player_cards in game.get_cards_of_all_players().items():
            messages.append(f"{player_name}'s cards are: {player_cards}")

        # calculating winner
        messages.append("\nCalculating winner of the game based off current hands...")
        best_hand = game.calculate_best_hand()
        messages.append(f"The winner of this game is: {best_hand[0]}.")
        messages.append(f"The winning hand is: {best_hand[1]}.")
        messages.append(f"The cards are: {best_hand[2]}.")

        return messages

    else:
        return ["Message $join to join a game if there's one available."]

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
    '$help': Command('Show the list of available commands.', show_help),
    '$join': Command('Lets you join a game that is already created but hasn\'t started.', join_game),
    '$startgame': Command('Lets you start a game if there are at least 2 players waiting to play.', start_game),
    # currently speed up the process of the game, no bets allowed just final showdown between all players
    '$playgame': Command('Showdown of best hand between players in the game.', play_game)
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
