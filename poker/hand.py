from poker.hand_validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator
)

class Hand:
    """
    This class represents the current hand of a player at each state of the game.

    Should be able to determine the best hand given the cards in current hand.
    """

    _VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator
    )

    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        """
        to add a list of cards to the current hand, for initial round, and for additional community cards.
        """
        cards_copy = self.cards[:]
        cards_copy.extend(cards)
        cards_copy.sort()
        self.cards = cards

    def best_hand(self):
        for validator_class in self._VALIDATORS:
            validator = validator_class(self.cards)

            # check to see if current cards can formulate the hand of the respective class
            if validator.is_valid():
                # return the name of the class, and the cards that make up the hand
                return (validator.name, validator.valid_cards())
