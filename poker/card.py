from collections import namedtuple

# holds the value of a card
CardValue = namedtuple("CardValue", ["rank_index", "suit_index"])


class Card:
    """
    This class represents a Card object in the game of Poker.
    Card has a rank and suit.
    """

    # possible suits belonging to a card
    SUITS = (
        "Clubs",
        "Diamonds",
        "Hearts",
        "Spades"
    )

    # possible ranks belonging to a card
    RANKS = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
    )

    def __init__(self, rank, suit):
        # rank and suit must be one of the items in their respective tuples to be valid
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")

        self.rank = rank
        self.suit = suit
        # store the position of the rank index in the tuple to perform comparisons
        self.card_value = CardValue(self.RANKS.index(self.rank), self.SUITS.index(self.suit))

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.card_value.suit_index < other.card_value.suit_index
        return self.card_value.rank_index < other.card_value.rank_index
