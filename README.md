# Texas Hold'em Discord Bot with Python

## Description
A simple discord bot that allows users in a Discord server to enjoy a quick game of **Texas Hold'em**.

This bot has logic implemented for the ten hands that players could get in a regular poker game, and follows the traditional rules. It requires at least 2 players to join in order to start the game.

## Installation

### Without Docker
Clone this repository, install the dependencies noted in the **requirements.txt** file using **pip**. Once everything is installed, create a **.env** file and add the following entry: BOT_TOKEN=**_Your_discord_bot_token_**. Note that you will have to provide your own discord bot token. 

Run the following command to start up the application:
```bash
python poker_bot.py
```

### With Docker
Clone the repository. Again, create a **.env** file and add the following entry: BOT_TOKEN=**_Your_discord_bot_token_**. Note that you will have to provide your own discord bot token. Build the docker image using ```docker build -t discord-poker-bot .``` Then run the image using ```docker run discord-poker-bot```.

## Usage
Once you see the bot appear in your discord server, you can use command 
```$help``` to get a list of different commands to get started with the game.

## Things to work on in the future
The current version of the application:
- Will keep listening to different user messages as invalid commands if it doesn't match one of the specific commands.
- Automates the entire process of the poker rounds (won't allow users to decide to place bet, fold, etc).
- Prints out every players cards at the end for each round due to the automated process.

A future version should look to tackle all of these inconveniences to simulate a more realistic poker game.
