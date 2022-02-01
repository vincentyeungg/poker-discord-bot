import pytest

from poker.player import Player
from poker.hand import Hand
from poker.card import Card


@pytest.fixture
def testing_cards():
    return [
        Card(rank="3", suit="Clubs"),
        Card(rank="7", suit="Clubs"),
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Hearts"),
        Card(rank="9", suit="Clubs"),
        Card(rank="10", suit="Diamonds"),
        Card(rank="Jack", suit="Clubs")
    ]

@pytest.fixture
def player():
    name = "Test Player 1"

    player = Player(name=name)

    return player


def test_create_player_and_store_name_and_hand_and_balance(testing_cards, player):
    player.add_cards(testing_cards)

    assert player.name == "Test Player 1"
    assert player.hand.cards == testing_cards


def test_player_initial_hand_is_empty(player):
    assert player.hand.cards == []


def test_player_will_play_initially(player):
    assert player.play


def test_player_can_add_cards_into_hand():
    name = "Test Player 1"
    player = Player(name=name)

    cards = [Card(rank="2", suit="Clubs"), Card(rank="7", suit="Diamonds")]

    player.add_cards(cards)

    assert player.hand.cards == [Card(rank="2", suit="Clubs"), Card(rank="7", suit="Diamonds")]


def test_obtain_best_hand_based_on_cards_from_collection(testing_cards, player):
    player.add_cards(testing_cards)

    # depends on the testing cards hand
    assert player.best_hand_name() == "Flush"


def test_obtain_cards_that_make_up_the_best_hand(testing_cards, player):
    player.add_cards(testing_cards)

    # depends on the testing cards hand
    assert player.best_hand_cards() == [
        Card(rank="3", suit="Clubs"),
        Card(rank="7", suit="Clubs"),
        Card(rank="8", suit="Clubs"),
        Card(rank="9", suit="Clubs"),
        Card(rank="Jack", suit="Clubs")
    ]


def test_player_wants_to_fold(player):
    player.wants_to_fold()

    # if a player folds, play flag set to false
    assert player.play == False


def test_player_makes_bet_with_valid_amount(player):
    player.place_bet(50.0)
    assert player.balance == 50.0


def test_player_makes_bet_with_invalid_amount(player):
    assert player.place_bet(200.0) == -1


def test_player_enters_invalid_amount(player):
    assert player.place_bet(-50.0) == -1