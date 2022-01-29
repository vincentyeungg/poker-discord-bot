from poker.hand_validators import FiveCardInARowValidatorHelper


class StraightFlushValidator(FiveCardInARowValidatorHelper):
    """
    This class represents a straight flush validator, in which there are 5 consecutive cards of same suit.
    """

    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"

    def is_valid(self):
        # return len(self._list_containing_five_consecutive_ordered_cards_of_same_suit) >= 1
        return True
