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

    def __init__(self):
        # when a game is initiated, no cards and players are created yet
        self.players = []
        self.deck = Deck()
        self.bet_accumulated = 0.0
        self.state = GameState.NO_GAME
        self.dealer = None

    def _awaiting_players_to_join(self):
        # wait for a list of accumulated players
        self.state = GameState.WAITING_FOR_PLAYERS

    def start_game(self):
        self.state = GameState.WAITING_FOR_INITIAL_CARDS_TO_BE_DEALT
        # initiate a starting deck
        cards = Card.generate_standard_52_cards()
        # shuffle the starting standard deck
        self.deck.add_cards(cards)
        self.deck.shuffle_cards()

    def add_player(self, player_name):
        # ensure there is only 1 player that joins
        if self.is_player_in_game(player_name):
            return False
        new_player = Player(player_name)
        self.players.append(new_player)
        return True

    def is_player_in_game(self, player_name):
        # checks if a player is already in the game
        for player in self.players:
            if player.name == player_name:
                return True
        return False

    def remove_player_from_game(self, player_name):
        # in case they want to fold
        # need to check who is the dealer, and if dealer folds, assign next player as dealer
        # might need to rework logic here
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
        return True

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

    def get_cards_of_all_players(self):
        return {player.name: player.hand for player in self.players}

    def _update_current_bets(self, amount):
        self.bet_accumulated += amount

    def calculate_best_hand(self):
        best_hand = None
        best_hand_idx = 11
        for player in self.players:
            # need to implement better hand comparisons to refine this logic
            player_hand_idx = player.best_hand()[0]
            if player_hand_idx < best_hand_idx:
                best_hand_idx = player_hand_idx
                best_hand = (player.name, player.best_hand_name(), player.best_hand_cards())

        return best_hand