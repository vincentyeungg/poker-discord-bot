import pytest

from poker.card import Card
from poker.hand_validators import TwoPairValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted

    return [
        Card(rank="3", suit="Clubs"),
        Card(rank="6", suit="Clubs"),
        Card(rank="6", suit="Diamonds"),
        Card(rank="7", suit="Hearts"),
        Card(rank="10", suit="Spades"),
        Card(rank="Queen", suit="Clubs"),
        Card(rank="Queen", suit="Spades")
    ]


def test_validates_hand_is_two_pair(testing_cards):
    validator = TwoPairValidator(testing_cards)

    assert validator.is_valid()


def test_returns_two_pair_name(testing_cards):
    validator = TwoPairValidator(cards=testing_cards)
    assert validator.name == "Two Pair"


def test_returns_two_pair_from_hand(testing_cards):
    validator = TwoPairValidator(testing_cards)

    six_of_clubs = Card(rank="6", suit="Clubs")
    six_of_diamonds = Card(rank="6", suit="Diamonds")
    queen_of_clubs = Card(rank="Queen", suit="Clubs")
    queen_of_spades = Card(rank="Queen", suit="Spades")

    # return the cards that were identified as a pair (2 cards of the same rank)
    assert validator.valid_cards() == [six_of_clubs, six_of_diamonds, queen_of_clubs, queen_of_spades]
