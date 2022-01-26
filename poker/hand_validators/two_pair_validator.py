from poker.hand_validators import ValidatorHelpers


class TwoPairValidator(ValidatorHelpers):
    """
    This class represents the Two Pair hand in poker in which your hand consists of at least 2 pairs and no other greater hand
    """

    def __init__(self, cards):
        super().__init__()
        self.cards = cards
        self.name = "Two Pair"

    def is_valid(self):
        # returns true if there are more than 2 pairs of cards of same rank found in current hand
        return len(self._ranks_with_counts(2)) >= 2

    def valid_cards(self):
        # returns the highest pair of cards
        # (2, Clubs), (2, Spades), (5, Diamonds), (5, Spades), (9, Diamonds), (9, Spades) returns
        # -> [(5, Diamonds), (5, Spades), (9, Diamonds), (9, Spades)]

        pairs_found = self._ranks_with_counts(2)  # {"2": 3, "5": 2, "9": 2}
        # since the cards are sorted, return the last 4 cards found to be a Pair (hand could have 3 possible pairs)
        return [card for card in self.cards if card.rank in pairs_found][-4:]