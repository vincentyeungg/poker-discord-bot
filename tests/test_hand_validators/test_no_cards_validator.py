import pytest

from poker.hand_validators import NoCardsValidator


@pytest.fixture
def testing_cards():
    # testing cards to validate no_cards_hand
    return []


def test_validates_hand_is_no_cards_hand(testing_cards):
    validator = NoCardsValidator(cards=testing_cards)
    # for no_cards_hand, there should be no cards (an empty list)
    assert validator.is_valid()


def test_returns_no_hand_name(testing_cards):
    validator = NoCardsValidator(cards=testing_cards)
    assert validator.name == "No Cards"


def test_returns_cards_for_valid_no_cards_hand(testing_cards):
    validator = NoCardsValidator(cards=testing_cards)
    assert validator.valid_cards() == []
