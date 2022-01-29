import pytest

from poker.card import Card
from poker.hand_validators import FullHouseValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted

    return [
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Diamonds"),
        Card(rank="8", suit="Spades"),
        Card(rank="Jack", suit="Hearts"),
        Card(rank="Jack", suit="Spades"),
        Card(rank="Queen", suit="Diamonds"),
        Card(rank="Queen", suit="Spades")
    ]


def test_validate_full_house_hand_in_collection(testing_cards):
    validator = FullHouseValidator(testing_cards)

    assert validator.is_valid()


def test_returns_full_house_name(testing_cards):
    validator = FullHouseValidator(testing_cards)
    assert validator.name == "Full House"


def test_returns_full_house_cards_in_hand(testing_cards):
    validator = FullHouseValidator(testing_cards)

    assert validator.valid_cards() == [
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Diamonds"),
        Card(rank="8", suit="Spades"),
        Card(rank="Queen", suit="Diamonds"),
        Card(rank="Queen", suit="Spades")
    ]


