import pytest

from poker.card import Card
from poker.hand_validators import StraightFlushValidator


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted

    six_of_clubs = Card(rank="6", suit="Clubs")
    seven_of_clubs = Card(rank="7", suit="Clubs")
    eight_of_clubs = Card(rank="8", suit="Clubs")
    eight_of_spades = Card(rank="8", suit="Spades")
    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_clubs = Card(rank="10", suit="Clubs")
    jack_of_clubs = Card(rank="Jack", suit="Clubs")

    return [
        six_of_clubs,
        seven_of_clubs,
        eight_of_clubs,
        eight_of_spades,
        nine_of_clubs,
        ten_of_clubs,
        jack_of_clubs
    ]


def test_validate_straight_flush_hand_in_collection(testing_cards):
    validator = StraightFlushValidator(testing_cards)

    assert validator.is_valid()


def test_returns_straight_flush_name(testing_cards):
    validator = StraightFlushValidator(testing_cards)
    assert validator.name == "Straight Flush"


def test_returns_straight_flush_cards_in_hand(testing_cards):
    validator = StraightFlushValidator(testing_cards)

    seven_of_clubs = Card(rank="7", suit="Clubs")
    eight_of_clubs = Card(rank="8", suit="Clubs")
    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_clubs = Card(rank="10", suit="Clubs")
    jack_of_clubs = Card(rank="Jack", suit="Clubs")

    assert validator.valid_cards() == [
        seven_of_clubs, eight_of_clubs, nine_of_clubs, ten_of_clubs, jack_of_clubs
    ]
