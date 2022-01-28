class CardOfSameSuitValidatorHelper:
    """
    Helper class that can be inherited by flush classes to determine if hand contains a valid flush.
    Contains properties of a flush hand.
    :return:
    """

    def __init__(self, cards):
        self.cards = cards

    @property
    def _card_suit_counts(self):
        """ build dictionary to hold occurrences of cards suit seen to formulate best hand """
        card_suit_counts = {}
        for card in self.cards:
            if card.suit in card_suit_counts:
                card_suit_counts[card.suit] += 1
            else:
                card_suit_counts[card.suit] = 1
        return card_suit_counts

    @property
    def _suits_that_occur_5_or_more_times(self):
        # return the suit of the cards in the hands, in which there is at least 5 of the same cards to be a flush
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
