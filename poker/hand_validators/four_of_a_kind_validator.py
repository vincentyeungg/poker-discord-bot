from poker.hand_validators import ValidatorHelpers


class FourOfAKindValidator(ValidatorHelpers):
    """
    This class represents a four of a kind hand.

    Consists of 4 cards of the same rank.
    """

    def __init__(self, cards):
        self.cards = cards
        self.name = "Four of a Kind"

    def is_valid(self):
        # if there is a rank identified with 4 occurrences in the hand, then this is valid
        return len(self._ranks_with_counts(4)) == 1

    def valid_cards(self):
        four_of_a_kind_cards = [card for card in self.cards if card.rank in self._ranks_with_counts(4)]
        return four_of_a_kind_cards
