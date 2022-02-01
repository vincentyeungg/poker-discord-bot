import pytest

from poker.player import Player
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.game import Game

@pytest.fixture
def testing_objs():
    # create test player 1
    test_player1 = "Player1"
    # create test player 2
    test_player2 = "Player2"
    # init deck
    test_deck = Deck()
    # create game object
    test_game = Game()
    test_players = [test_player1, test_player2]

    return {
        "players": test_players,
        "deck": test_deck,
        "game": test_game
    }

def test_game_starts_with_no_players_and_cards_and_deck_and_bet_accumulated(testing_objs):
    game = testing_objs.get("game")
    assert len(game.players) == 0
    assert len(game.deck) == 0
    assert game.bet_accumulated == 0.0

def test_can_add_player_to_game(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])

    assert len(game.players) == 2

def test_start_game_and_add_players_and_cards_into_game(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()

    assert len(game.players) == 2
    assert len(game.deck) == 52

def test_players_have_names_in_game(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])

    assert game.players[0].name == "Player1"

def test_verify_game_cannot_add_player_with_same_name(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])

    # should not be able to add new player with same name
    assert game.add_player(players[0]) == False

def test_verify_get_current_cards_of_all_player(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])

    game.start_game()
    game.hand_out_initial_two_cards_to_players()

    assert game.get_cards_of_all_players() == {players[0]: game.players[0].hand}

def test_hand_out_2_cards_to_each_player_in_the_game(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()
    game.hand_out_initial_two_cards_to_players()

    for player in game.players:
        assert len(player.hand) == 2

def test_hand_out_three_community_cards_to_each_player_in_the_game_during_flop(testing_objs):
    # the cards handed out in flop round must be the same
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()
    game.hand_out_three_community_cards_to_all_players()

    for player in game.players:
        assert len(player.hand) == 3

def test_hand_out_turn_cards_to_each_player_during_turn(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()
    game.hand_out_turn_card_to_all_players()

    for player in game.players:
        assert len(player.hand) == 1

def test_hand_out_river_cards_to_each_player_during_turn(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()
    game.hand_out_river_card_to_all_players()

    for player in game.players:
        assert len(player.hand) == 1

def test_assert_all_players_have_7_cards_in_their_hand_after_all_rounds(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()

    # dealer will hand out 7 cards in total (5 cards are shared)
    game.hand_out_initial_two_cards_to_players()
    game.hand_out_three_community_cards_to_all_players()
    game.hand_out_turn_card_to_all_players()
    game.hand_out_river_card_to_all_players()

    for player in game.players:
        assert len(player.hand) == 7

def test_assert_all_player_community_cards_are_the_same(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()

    # dealer will hand out 7 cards in total (5 cards are shared)
    game.hand_out_initial_two_cards_to_players()
    game.hand_out_three_community_cards_to_all_players()
    game.hand_out_turn_card_to_all_players()
    game.hand_out_river_card_to_all_players()

    # take the community cards from a player and check if all players have same community cards
    community_cards_seen = set()
    community_cards = []

    for player in game.players:
        for card in player.hand.cards:
            if str(card) in community_cards_seen:
                community_cards.append(card)
            else:
                community_cards_seen.add(str(card))

    assert len(community_cards) == 5

def test_players_want_to_make_bets(testing_objs):
    game = testing_objs.get("game")
    players = testing_objs.get("players")
    game.add_player(players[0])
    game.add_player(players[1])
    game.start_game()

    game.hand_out_initial_two_cards_to_players()

    # after cards are dealt, players will be asked if they want to place bets or fold
    player1_amount_bet = game.players[0].place_bet(50.0)
    player2_amount_bet = game.players[1].place_bet(85.0)

    total_betting = sum([player1_amount_bet, player2_amount_bet])
    game._update_current_bets(total_betting)

    assert game.bet_accumulated == 135.0

def test_player_wants_to_fold(testing_objs):
    pass