import pytest

from poker.card import Card
from poker.hand_validators import StraightValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted
    # it is possible to have 2 of 3 same ranked cards

    return [
        Card(rank="6", suit="Clubs"),
        Card(rank="7", suit="Diamonds"),
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Hearts"),
        Card(rank="9", suit="Clubs"),
        Card(rank="10", suit="Diamonds"),
        Card(rank="Jack", suit="Spades")
    ]


def test_validates_hand_is_straight(testing_cards):
    validator = StraightValidator(testing_cards)

    assert validator.is_valid()


def test_returns_straight_name(testing_cards):
    validator = StraightValidator(cards=testing_cards)
    assert validator.name == "Straight"


def test_returns_straight_from_hand(testing_cards):
    validator = StraightValidator(testing_cards)

    # return the highest cards identified as straight
    assert validator.valid_cards() == [
        # results depend on what you feed in as testing_cards
        Card(rank="7", suit="Diamonds"),
        Card(rank="8", suit="Hearts"),
        Card(rank="9", suit="Clubs"),
        Card(rank="10", suit="Diamonds"),
        Card(rank="Jack", suit="Spades")
    ]
