from poker.hand_validators import ValidatorHelpers


class PairValidator(ValidatorHelpers):
    """
    Represents a Pair in poker, when a player contains 2 cards of the same rank.
    """

    def __init__(self, cards):
        super().__init__()
        self.cards = cards
        self.name = "Pair"

    def is_valid(self):
        # ensure there is only 1 pair in the hand
        pair_of_ranks = self._ranks_with_counts(2)
        return len(pair_of_ranks) == 1

    def valid_cards(self):
        # return the cards as identified as a pair
        return [card for card in self.cards if card.rank in self._ranks_with_counts(2)]
