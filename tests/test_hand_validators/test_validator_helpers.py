import pytest

from poker.card import Card
from poker.hand_validators import ValidatorHelpers


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted
    # it is possible to have 2 of 3 same ranked cards

    return [
        Card(rank="6", suit="Clubs"),
        Card(rank="7", suit="Diamonds"),
        Card(rank="8", suit="Clubs"),
        Card(rank="8", suit="Hearts"),
        Card(rank="9", suit="Clubs"),
        Card(rank="Jack", suit="Diamonds"),
        Card(rank="Ace", suit="Spades")
    ]


def test_store_ranks_count(testing_cards):
    validator_helper = ValidatorHelpers(testing_cards)

    assert validator_helper._card_rank_counts == {
        "6": 1,
        "7": 1,
        "8": 2,
        "9": 1,
        "Jack": 1,
        "Ace": 1
    }


def test_get_stored_ranks_with_specific_count(testing_cards):
    validator_helper = ValidatorHelpers(testing_cards)

    assert validator_helper._ranks_with_counts(2) == {"8": 2}
    assert validator_helper._ranks_with_counts(1) == {
        "6": 1,
        "7": 1,
        "9": 1,
        "Jack": 1,
        "Ace": 1
    }
