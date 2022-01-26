import pytest

from poker.card import Card
from poker.hand_validators import HighCardValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)
    queen_of_spades = Card(rank="Queen", suit="Spades")

    # assume all cards at this point are sorted

    return [
        Card(rank="3", suit="Clubs"),
        Card(rank="5", suit="Diamonds"),
        Card(rank="6", suit="Clubs"),
        Card(rank="7", suit="Hearts"),
        Card(rank="10", suit="Spades"),
        Card(rank="Jack", suit="Clubs"),
        queen_of_spades
    ]


def test_validates_hand_is_high_card(testing_cards):
    validator = HighCardValidator(testing_cards)

    assert validator.is_valid()


def test_returns_high_card_name(testing_cards):
    validator = HighCardValidator(cards=testing_cards)
    assert validator.name == "High Card"


def test_returns_high_card_from_hand(testing_cards):
    validator = HighCardValidator(testing_cards)

    # assuming that the hand is sorted, it will return the single highest card in the hand
    assert validator.valid_cards() == testing_cards[-1]
