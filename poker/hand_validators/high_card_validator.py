from poker.hand_validators import ValidatorHelpers


class HighCardValidator(ValidatorHelpers):
    """
    Representation of a high card hand, and is the lowest ranked hand in the game other than no cards.
    """

    def __init__(self, cards):
        super().__init__(cards)
        self.cards = cards
        self.name = "High Card"

    def is_valid(self):
        # if the card_rank_count dict has same number of keys as cards in the hand, and no other validators are valid
        return len(self._card_rank_counts) != 0 and len(self._card_rank_counts) == len(self.cards)

    def valid_cards(self):
        # if this validator is invalid, then it will move to the next hand validator in the logic
        return self.cards[-1]
