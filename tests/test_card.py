from poker.card import Card

import pytest

@pytest.fixture
def nine_of_spades():
    return Card(rank="9", suit="Spades")


def test_can_create_card_with_valid_parameters(nine_of_spades):
    # create card with valid parameters
    assert nine_of_spades.rank == "9" and nine_of_spades.suit == "Spades"


def test_exception_thrown_when_creating_card_with_invalid_rank_parameters():
    # make sure exception is raised if rank parameter isn't valid
    with pytest.raises(ValueError) as ex:
        card1 = Card(rank=9, suit="Spades")
    assert "Invalid rank. Rank must be one of the following: " in str(ex.value)


def test_exception_thrown_when_creating_card_with_invalid_suit_parameters():
    # make sure exception is raised if suit parameter isn't valid
    with pytest.raises(ValueError) as ex:
        card1 = Card(rank="9", suit="Spade")
    assert "Invalid suit. Suit must be one of the following: " in str(ex.value)


def test_card_has_card_value_of_rank_and_suit(nine_of_spades):
    # card value made up of the rank and suit
    assert nine_of_spades.card_value == (7, 3)


def test_has_string_representation_with_suit_and_rank(nine_of_spades):
    # override the __str__()
    assert str(nine_of_spades) == "9 of Spades"


def test_card_has_four_possible_suit_options():
    # ensure only suit options allowed are as shown
    assert Card.SUITS == ("Clubs", "Diamonds", "Hearts", "Spades")


def test_card_has_thirteen_possible_rank_options():
    # ensure only rank options allowed are as shown
    assert Card.RANKS == (
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
    )


def test_figures_out_if_two_cards_are_equal(nine_of_spades):
    # override __eq__()
    assert nine_of_spades == Card(rank="9", suit="Spades")


def test_figures_out_if_one_card_is_greater_than_another_card():
    # should be able to compare cards and conclude one card is greater than the other if they aren't equal
    assert Card(rank="7", suit="Spades") < Card(rank="9", suit="Spades")
    assert Card(rank="5", suit="Clubs") < Card(rank="Ace", suit="Hearts")
    # suits values are in order of Spades > Hearts > Diamonds > Clubs
    assert Card(rank="9", suit="Hearts") < Card(rank="9", suit="Spades")


