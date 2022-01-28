import pytest

from poker.card import Card
from poker.hand_validators import FiveCardInARowValidatorHelper


@pytest.fixture
def testing_cards():
    # a hand can have up to 7 cards (including community cards)

    # assume all cards at this point are sorted
    # it is possible to have 2 of 3 same ranked cards

    six_of_clubs = Card(rank="6", suit="Clubs")
    seven_of_diamonds = Card(rank="7", suit="Diamonds")
    eight_of_clubs = Card(rank="8", suit="Clubs")
    eight_of_hearts = Card(rank="8", suit="Hearts")
    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_diamonds = Card(rank="10", suit="Diamonds")
    jack_of_spades = Card(rank="Jack", suit="Spades")

    return [
        six_of_clubs,
        seven_of_diamonds,
        eight_of_clubs,
        eight_of_hearts,
        nine_of_clubs,
        ten_of_diamonds,
        jack_of_spades
    ]


def test_store_cards_of_same_ranks_in_a_dict_of_lists(testing_cards):
    validator = FiveCardInARowValidatorHelper(testing_cards)

    six_of_clubs = Card(rank="6", suit="Clubs")
    seven_of_diamonds = Card(rank="7", suit="Diamonds")
    eight_of_clubs = Card(rank="8", suit="Clubs")
    eight_of_hearts = Card(rank="8", suit="Hearts")
    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_diamonds = Card(rank="10", suit="Diamonds")
    jack_of_spades = Card(rank="Jack", suit="Spades")

    assert validator._dict_of_ranks_storing_lists_of_cards_of_the_same_rank == {
        "6": [six_of_clubs],
        "7": [seven_of_diamonds],
        "8": [eight_of_clubs, eight_of_hearts],
        "9": [nine_of_clubs],
        "10": [ten_of_diamonds],
        "Jack": [jack_of_spades]
    }


def test_validate_indices_are_increasing_and_in_consecutive_order(testing_cards):
    valid_straight_indices = [3, 4, 5, 6, 7]
    validator = FiveCardInARowValidatorHelper(testing_cards)

    assert validator._every_element_increasing_by_one(valid_straight_indices)


def test_validate_indices_are_not_increasing_and_in_consecutive_order(testing_cards):
    invalid_straight_indices = [3, 5, 6, 7, 8]
    validator = FiveCardInARowValidatorHelper(testing_cards)

    assert not validator._every_element_increasing_by_one(invalid_straight_indices)


def test_filter_cards_in_dictionary_and_retrieve_highest_valued_card_for_each_rank(testing_cards):
    six_of_clubs = Card(rank="6", suit="Clubs")
    seven_of_diamonds = Card(rank="7", suit="Diamonds")
    eight_of_hearts = Card(rank="8", suit="Hearts")
    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_diamonds = Card(rank="10", suit="Diamonds")
    jack_of_spades = Card(rank="Jack", suit="Spades")

    validator = FiveCardInARowValidatorHelper(testing_cards)

    assert validator._list_containing_highest_valued_card_of_each_rank == [
        six_of_clubs, seven_of_diamonds, eight_of_hearts, nine_of_clubs, ten_of_diamonds, jack_of_spades
    ]


def test_returns_collection_of_lists_of_valid_straight_hand_from_hand(testing_cards):
    validator = FiveCardInARowValidatorHelper(testing_cards)

    six_of_clubs = Card(rank="6", suit="Clubs")
    seven_of_diamonds = Card(rank="7", suit="Diamonds")
    eight_of_hearts = Card(rank="8", suit="Hearts")
    nine_of_clubs = Card(rank="9", suit="Clubs")
    ten_of_diamonds = Card(rank="10", suit="Diamonds")
    jack_of_spades = Card(rank="Jack", suit="Spades")

    assert validator._collections_of_five_straight_cards_in_a_row == [
        [six_of_clubs, seven_of_diamonds, eight_of_hearts, nine_of_clubs, ten_of_diamonds],
        [seven_of_diamonds, eight_of_hearts, nine_of_clubs, ten_of_diamonds, jack_of_spades]
    ]
