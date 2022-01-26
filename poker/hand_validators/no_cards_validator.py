class NoCardsValidator:
    """
    Representation of a No Cards hand in which a player doesn't have any cards to constitute to a hand

    Happens at the start of the game when no cards are dealt, and when a player forfeits.
    """

    def __init__(self, cards):
        self.cards = cards
        self.name = "No Cards"

    def is_valid(self):
        return len(self.cards) == 0

    def valid_cards(self):
        return self.cards
    