from poker.hand_validators import CardOfSameSuitValidatorHelper


class FlushValidator(CardOfSameSuitValidatorHelper):
    """
    This class represents a flush hand in poker, where all the cards are of the same suit.
    """

    def __init__(self, cards):
        self.cards = cards
        self.name = "Flush"

    def is_valid(self):
        # need to check if there are 5 cards that are of the same suit
        return len(self._suits_that_occur_5_or_more_times) == 1

    def valid_cards(self):
        # iterate cards against the suit that is returned from the dictionary that detected 5 same suits
        valid_flush = [card for card in self.cards if card.suit in self._suits_that_occur_5_or_more_times]
        # if the hand contains more than 5 same suit cards, return the 5 greatest cards (last 5)
        return valid_flush[-5:]
