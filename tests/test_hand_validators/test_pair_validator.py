import pytest

from poker.card import Card
from poker.hand_validators import PairValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)
    queen_of_clubs = Card(rank="Queen", suit="Clubs")
    queen_of_spades = Card(rank="Queen", suit="Spades")

    # assume all cards at this point are sorted

    return [
        Card(rank="3", suit="Clubs"),
        Card(rank="5", suit="Diamonds"),
        Card(rank="6", suit="Clubs"),
        Card(rank="7", suit="Hearts"),
        Card(rank="10", suit="Spades"),
        queen_of_clubs,
        queen_of_spades
    ]


def test_validates_hand_is_pair(testing_cards):
    validator = PairValidator(testing_cards)

    assert validator.is_valid()


def test_returns_high_card_name(testing_cards):
    validator = PairValidator(cards=testing_cards)
    assert validator.name == "Pair"


def test_returns_high_card_from_hand(testing_cards):
    validator = PairValidator(testing_cards)

    queen_of_clubs = Card(rank="Queen", suit="Clubs")
    queen_of_spades = Card(rank="Queen", suit="Spades")

    # return the cards that were identified as a pair (2 cards of the same rank)
    assert validator.valid_cards() == [queen_of_clubs, queen_of_spades]
