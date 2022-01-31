from random import shuffle


class Deck:
    """
    Representation of a deck in a poker game.

    A deck consists of 52 cards total with the ability to draw cards from deck and assign to different players.
    """

    def __init__(self):
        # initially instantiation of deck object at the start of game, the deck will just be an empty list with no cards
        self.cards = []

    def __len__(self):
        # the length of a deck is determined by the number of cards currently in the deck
        return len(self.cards)

    def add_cards(self, cards):
        # should accept a list of cards, and add those individual cards into the existing deck of cards
        self.cards.extend(cards)

    def remove_cards(self, number_of_cards):
        # this removes the cards from the end of the deck of cards, and returns the removed cards
        if number_of_cards < 1:
            raise ValueError("You must remove at least 1 card")
        removed_cards = self.cards[-1 * number_of_cards:]
        del self.cards[-1 * number_of_cards:]
        return removed_cards

    def shuffle_cards(self):
        shuffle(self.cards)