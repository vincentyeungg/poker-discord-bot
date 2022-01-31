from enum import Enum

from poker.player import Player
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand

class GameState(Enum):
    # game hasn't started yet
    NO_GAME = 1
    # a game was initiated, waiting for players to join
    WAITING_FOR_PLAYERS = 2
    # after all players join the game, they will be 'seated' and waiting for dealer to deal 2 cards to them
    WAITING_FOR_INITIAL_CARDS_TO_BE_DEALT = 3
    # once players have their starting 2 cards, they can begin making their bets
    PLAYERS_HAS_CARDS = 4
    # after first round of betting, the flop round (3 community cards) are dealt
    FLOP_DEALT = 5
    # turn round (1 community card) is dealt
    TURN_DEALT = 6
    # river round (1 community card) is dealt
    RIVER_DEALT = 7


class Game:
    """
    This class represents the game of poker which consists of players, cards, decks and a sum accumulation of bets.
    """

    def __init__(self, deck):
        # when a game is initiated, no cards and players are created yet
        self.players = []
        self.deck = deck
        self.bet_accumulated = 0.0

    def start_game(self, players):
        # get a list of players and add it in the players list of the game
        self.players.extend(players)
        # initiate a starting deck
        cards = Card.generate_standard_52_cards()
        # shuffle the starting standard deck
        self.deck.add_cards(cards)
        self.deck.shuffle_cards()

    def hand_out_initial_two_cards_to_players(self):
        # iterate through each player and add two cards from the current deck
        for player in self.players:
            # remove 2 cards from the deck
            player_cards = self.deck.remove_cards(2)
            player.add_cards(player_cards)

    def hand_out_three_community_cards_to_all_players(self):
        self._hand_out_community_cards(3)

    def hand_out_turn_card_to_all_players(self):
        self._hand_out_community_cards(1)

    def hand_out_river_card_to_all_players(self):
        self._hand_out_community_cards(1)

    def _hand_out_community_cards(self, number_of_cards):
        # cards handed out here must be the same
        flop_cards = self.deck.remove_cards(number_of_cards)

        for player in self.players:
            player.add_cards(flop_cards)

    def _update_current_bets(self, amount):
        self.bet_accumulated += amount