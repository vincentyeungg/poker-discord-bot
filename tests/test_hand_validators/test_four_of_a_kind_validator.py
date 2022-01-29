import pytest

from poker.card import Card
from poker.hand_validators import FourOfAKindValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted

    return [
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Diamonds"),
        Card(rank="8", suit="Hearts"),
        Card(rank="8", suit="Spades"),
        Card(rank="Jack", suit="Spades"),
        Card(rank="Queen", suit="Diamonds"),
        Card(rank="Queen", suit="Spades")
    ]


def test_validate_four_of_a_kind_hand_in_collection(testing_cards):
    validator = FourOfAKindValidator(testing_cards)

    assert validator.is_valid()


def test_returns_four_of_a_kind_name(testing_cards):
    validator = FourOfAKindValidator(testing_cards)
    assert validator.name == "Four of a Kind"


def test_returns_four_of_a_kind_cards_in_hand(testing_cards):
    validator = FourOfAKindValidator(testing_cards)

    assert validator.valid_cards() == [
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Diamonds"),
        Card(rank="8", suit="Hearts"),
        Card(rank="8", suit="Spades")
    ]
