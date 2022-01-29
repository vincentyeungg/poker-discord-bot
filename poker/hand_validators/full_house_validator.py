from poker.hand_validators import ValidatorHelpers


class FullHouseValidator(ValidatorHelpers):
    """
    This class represents a full house in poker.

    A full house consists of three cards of the same rank, and two cards of the same rank.
    """

    def __init__(self, cards):
        super().__init__(cards)
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        pair_cards = self._ranks_with_counts(2)
        three_of_a_kind_cards = self._ranks_with_counts(3)

        # possible to have 2 pairs and a 3 of a kind
        return len(three_of_a_kind_cards) == 1 and len(pair_cards) >= 1

    def valid_cards(self):
        # edge case is if there are 2 pairs and a three of a kind in the hand
        # return the pair of higher value along with the three of a kind
        pair_cards = self._ranks_with_counts(2)
        three_of_a_kind_cards = self._ranks_with_counts(3)
        flush_cards = [card for card in self.cards if card.rank == list(pair_cards.keys())[-1]]
        flush_cards.extend([card for card in self.cards if card.rank == list(three_of_a_kind_cards)[0]])

        # sort the cards since order might not be maintained
        flush_cards.sort()

        return flush_cards
