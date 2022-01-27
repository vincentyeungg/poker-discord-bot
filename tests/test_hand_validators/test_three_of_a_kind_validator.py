import pytest

from poker.card import Card
from poker.hand_validators import ThreeOfAKindValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted
    # it is possible to have 2 of 3 same ranked cards

    return [
        Card(rank="6", suit="Clubs"),
        Card(rank="6", suit="Diamonds"),
        Card(rank="6", suit="Spades"),
        Card(rank="7", suit="Hearts"),
        Card(rank="Queen", suit="Clubs"),
        Card(rank="Queen", suit="Diamonds"),
        Card(rank="Queen", suit="Spades")
    ]


def test_validates_hand_is_three_of_a_kind(testing_cards):
    validator = ThreeOfAKindValidator(testing_cards)

    assert validator.is_valid()


def test_returns_three_of_a_kind_name(testing_cards):
    validator = ThreeOfAKindValidator(cards=testing_cards)
    assert validator.name == "Three of a Kind"


def test_returns_three_of_a_kind_from_hand(testing_cards):
    validator = ThreeOfAKindValidator(testing_cards)

    # return the highest cards identified as three of a kind
    assert validator.valid_cards() == testing_cards[-3:]
