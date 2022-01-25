from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

import pytest


@pytest.fixture
def testing_cards():
    return [
        Card(rank="3", suit="Spades"),
        Card(rank="5", suit="Hearts"),
        Card(rank="Ace", suit="Spades")
    ]


def test_initial_deck_has_no_cards():
    # initially the deck will have no cards
    deck = Deck()
    assert deck.cards == []


def test_deck_has_length_equal_to_count_of_cards():
    # length of deck is how many cards are currently in the deck
    deck = Deck()
    assert len(deck) == 0


def test_can_add_cards_into_deck(testing_cards):
    # can add cards in deck, to be used in populating deck with 52 cards
    deck = Deck()
    deck.add_cards(testing_cards)
    assert len(deck) == 3
    assert deck.cards == testing_cards


def test_can_remove_cards_into_deck(testing_cards):
    # can remove cards from deck, to be used in 'handing' out cards to players in various states of the game
    deck = Deck()
    deck.add_cards(testing_cards)

    # when removing cards from the deck, it will remove from the end of the deck
    deck.remove_cards(2)

    # the deck will always return a list of cards, even if one or zero cards
    assert deck.cards == [
        # check if the remaining card is the third card from the end
        # testing_cards has 3 cards initially, removing 2 cards as specified should result in last 2 cards removed
        testing_cards[-3]
    ]


def test_returns_removed_cards_from_deck(testing_cards):
    # can remove cards from deck, to be used in 'handing' out cards to players in various states of the game
    deck = Deck()
    deck.add_cards(testing_cards)

    # when removing cards from the deck, it will remove from the end of the deck
    assert deck.remove_cards(2) == testing_cards[-2:]


def test_exception_thrown_if_removing_zero_or_negative_number_of_cards(testing_cards):
    # can remove cards from deck, to be used in 'handing' out cards to players in various states of the game
    deck = Deck()
    deck.add_cards(testing_cards)
    with pytest.raises(ValueError) as ex:
        deck.remove_cards(0)
    assert "You must remove at least 1 card" == str(ex.value)


@patch("poker.deck.shuffle")
def test_can_shuffle_current_hand_in_random_order(mock_shuffle, testing_cards):
    # can shuffle a deck randomly and differently
    deck = Deck()
    deck.add_cards(testing_cards)

    deck.shuffle()

    # assert random is called once
    mock_shuffle.assert_called_once_with(testing_cards)