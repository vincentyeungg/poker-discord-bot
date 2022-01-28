import pytest

from poker.card import Card
from poker.hand_validators import FlushValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted

    return [
        Card(rank="3", suit="Clubs"),
        Card(rank="7", suit="Clubs"),
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Hearts"),
        Card(rank="9", suit="Clubs"),
        Card(rank="10", suit="Diamonds"),
        Card(rank="Jack", suit="Clubs")
    ]


def test_validates_flush_hand_in_collection(testing_cards):
    validator = FlushValidator(testing_cards)

    assert validator.is_valid()


def test_returns_flush_name(testing_cards):
    validator = FlushValidator(testing_cards)
    assert validator.name == "Flush"


def test_returns_flush_from_hand(testing_cards):
    validator = FlushValidator(testing_cards)

    # return the highest cards identified as straight
    assert validator.valid_cards() == [
        # results depend on what you feed in as testing_cards
        Card(rank="3", suit="Clubs"),
        Card(rank="7", suit="Clubs"),
        Card(rank="8", suit="Clubs"),
        Card(rank="9", suit="Clubs"),
        Card(rank="Jack", suit="Clubs")
    ]
