from poker.hand_validators import ValidatorHelpers


class ThreeOfAKindValidator(ValidatorHelpers):
    """
    This class represents a 3 of a kind hand in poker in which a player has 3 cards of the same rank
    """

    def __init__(self, cards):
        super().__init__(cards)
        self.cards = cards
        self.name = "Three of a Kind"

    def is_valid(self):
        # a hand can have 2 possible Three of a kinds in which the player has i.e., 3 Six of Clubs, and 3 Ace of Spades
        # if a hand has 3 cards that have the same rank

        return len(self._ranks_with_counts(3)) >= 1

    def valid_cards(self):
        # return the highest cards that form the 3 of a kind
        possible_three_of_a_kinds = [card for card in self.cards if card.rank in self._ranks_with_counts(3)]
        # since the cards should be sorted, just return the last 3 cards (will take the highest valued cards)
        return possible_three_of_a_kinds[-3:]
