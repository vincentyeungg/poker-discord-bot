from poker.hand import Hand

class Player:
    """
    Represents a player in a game of poker. A player will have some balance to bet if they wish, and their cards.
    """

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.balance = 100.0 # default balance for now, everyone gets this amount to play the game
        self.play = True

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def best_hand(self):
        return self.hand.best_hand()

    def best_hand_name(self):
        # return the name of the hand identified as the best hand
        return self.hand.best_hand()[1]

    def best_hand_cards(self):
        # return the cards of the best identified as the best hand
        return self.hand.best_hand()[2]

    def wants_to_fold(self):
        # if player chooses to fold during a betting round, they will be removed from the game
        self.play = False

    def place_bet(self, amount):
        # take the amount from the current
        # check if the current player has enough balance to make the bet
        # if invalid amount, return False, else modify the balance and return True
        if not amount <= 0:
            if self.balance >= amount:
                self.balance -= amount
                return amount

        return -1
