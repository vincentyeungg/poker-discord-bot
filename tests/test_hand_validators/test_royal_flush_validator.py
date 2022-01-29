import pytest

from poker.card import Card
from poker.hand_validators import RoyalFlushValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted

    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_clubs = Card(rank="10", suit="Clubs")
    jack_of_clubs = Card(rank="Jack", suit="Clubs")
    queen_of_clubs = Card(rank="Queen", suit="Clubs")
    king_of_clubs = Card(rank="King", suit="Clubs")
    ace_of_clubs = Card(rank="Ace", suit="Clubs")
    ace_of_spades = Card(rank="Ace", suit="Spades")

    return [
        nine_of_clubs,
        ten_of_clubs,
        jack_of_clubs,
        queen_of_clubs,
        king_of_clubs,
        ace_of_clubs,
        ace_of_spades
    ]


def test_validate_royal_flush_hand_in_collection(testing_cards):
    validator = RoyalFlushValidator(testing_cards)

    assert validator.is_valid()


def test_returns_royal_flush_name(testing_cards):
    validator = RoyalFlushValidator(testing_cards)
    assert validator.name == "Royal Flush"


def test_returns_royal_flush_cards_in_hand(testing_cards):
    validator = RoyalFlushValidator(testing_cards)

    ten_of_clubs = Card(rank="10", suit="Clubs")
    jack_of_clubs = Card(rank="Jack", suit="Clubs")
    queen_of_clubs = Card(rank="Queen", suit="Clubs")
    king_of_clubs = Card(rank="King", suit="Clubs")
    ace_of_clubs = Card(rank="Ace", suit="Clubs")

    assert validator.valid_cards() == [
        ten_of_clubs,
        jack_of_clubs,
        queen_of_clubs,
        king_of_clubs,
        ace_of_clubs
    ]
