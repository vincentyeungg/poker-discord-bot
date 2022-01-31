import pytest

from poker.card import Card
from poker.hand import Hand

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


def test_hand_starts_out_with_no_cards():
    hand = Hand()
    assert hand.cards == []


def test_get_length_of_hand(testing_cards):
    hand = Hand()
    hand.add_cards(testing_cards)

    assert len(hand) == 7


def test_shows_current_hand_in_technical_representation():
    cards = [
        Card(rank="10", suit="Diamonds"),
        Card(rank="Jack", suit="Clubs")
    ]
    hand = Hand()
    hand.add_cards(cards)

    assert repr(hand) == "10 of Diamonds, Jack of Clubs"


def test_can_add_cards_to_hand(testing_cards):
    hand = Hand()
    hand.add_cards(testing_cards)
    assert hand.cards == testing_cards


def test_determines_best_hand_based_on_cards_in_current_collection(testing_cards):
    # the ranks follow best ranked hands from poker
    # royal flush is the best, and high card is the lowest worth hand
    hand = Hand()
    hand.add_cards(testing_cards)

    assert hand.best_hand() == (
        "Flush",
        [
            Card(rank="3", suit="Clubs"),
            Card(rank="7", suit="Clubs"),
            Card(rank="8", suit="Clubs"),
            Card(rank="9", suit="Clubs"),
            Card(rank="Jack", suit="Clubs")
        ]
    )
