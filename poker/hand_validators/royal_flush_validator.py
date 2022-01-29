from poker.hand_validators import FiveCardInARowValidatorHelper


class RoyalFlushValidator(FiveCardInARowValidatorHelper):
    """
    This class represents the best hand in poker in which your hand is a royal flush
    with Ace being the highest valued card.
    """

    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Flush"

    def is_valid(self):
        # royal flush is a special case of the straight flush
        possible_straight_flushes = self._list_containing_five_consecutive_ordered_cards_of_same_suit
        # cards are sorted (verified in other class tests for those methods)
        for straight_flush in possible_straight_flushes:
            if straight_flush[0].rank == "10" and straight_flush[-1].rank == "Ace":
                return True

        return False

    def valid_cards(self):
        possible_straight_flushes = self._list_containing_five_consecutive_ordered_cards_of_same_suit
        royal_flushes = []
        for cards in possible_straight_flushes:
            if cards[0].rank == "10" and cards[-1].rank == "Ace":
                royal_flushes.append(cards)

        # return the highest valued royal flush
        return royal_flushes[-1]
