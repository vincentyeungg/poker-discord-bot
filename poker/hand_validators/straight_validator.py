from poker.hand_validators import FiveCardInARowValidatorHelper


class StraightValidator(FiveCardInARowValidatorHelper):
    """
    This class represents a straight hand in which there are 5 cards of consecutive ranks.
    """

    def __init__(self, cards):
        super().__init__(cards)
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        # 5 consecutive cards of consecutive ranks would constitute a straight
        # since the cards are in order, iterate using a width of 5
        if len(self.cards) < 5:
            return False

        # get a list of possible straights
        possible_straights = self._collections_of_five_straight_cards_in_a_row

        # valid straight as long as there exists 5 consecutive cards that constitute a straight hand
        return len(possible_straights) > 0

    def valid_cards(self):
        # get a list of possible straights
        possible_straights = self._collections_of_five_straight_cards_in_a_row

        # return highest valued straight from a list of possible straights
        return possible_straights[-1]
