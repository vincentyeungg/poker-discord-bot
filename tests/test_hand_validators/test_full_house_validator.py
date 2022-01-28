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
        Card(rank="10", suit="Hearts"),
        Card(rank="Jack", suit="Clubs"),
        Card(rank="Queen", suit="Diamonds"),
        Card(rank="Queen", suit="Spades")
    ]