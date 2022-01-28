import pytest

from poker.card import Card
from poker.hand_validators import CardOfSameSuitValidatorHelper


@pytest.fixture
def testing_cards():
    return [
        Card(rank="3", suit="Clubs"),
        Card(rank="7", suit="Clubs"),
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Hearts"),
        Card(rank="9", suit="Clubs"),
        Card(rank="10", suit="Diamonds"),
        Card(rank="Jack", suit="Clubs")
    ]


def test_return_a_dictionary_of_suits_with_suits_occurrences(testing_cards):
    validator = CardOfSameSuitValidatorHelper(testing_cards)

    assert validator._card_suit_counts == {
        "Clubs": 5,
        "Hearts": 1,
        "Diamonds": 1
    }


def test_return_specific_suit_cards_with_specific_count(testing_cards):
    validator = CardOfSameSuitValidatorHelper(testing_cards)

    assert validator._suits_that_occur_5_or_more_times == {
        "Clubs": 5
    }
