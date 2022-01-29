class FiveCardInARowValidatorHelper:
    """
    Helper class for properties that belong to hands that consists of 5 cards of consecutive ranks.
    """

    def __init__(self, cards):
        self.cards = cards

    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        """ returns a list of lists that contain 5 cards of consecutive ranks """

        # edge case: 2 Clubs, 3 Diamonds, 3 Spades, 4 Clubs, 5 Spades, 6 Clubs, 6 Spades
        # above will be a straight of 2 Clubs, 3 Spades, 4 Clubs, 5 Spades, 6 Spades

        # if there aren't at least 5 unique ranks, then return an empty list
        if len(self._list_containing_highest_valued_card_of_each_rank) < 5:
            return []

        index = 0
        final_index = len(self._list_containing_highest_valued_card_of_each_rank) - 1
        collections_of_straights = []

        # loop in window size of 5, and determine if the current 5 card ranks make up a straight (consecutive ranks)
        while index + 4 <= final_index:
            next_five_cards = self._list_containing_highest_valued_card_of_each_rank[index: index + 5]
            next_five_indices = [card.card_value.rank_index for card in next_five_cards]

            # if a straight is detected, add this in the list of possible straights
            if self._every_element_increasing_by_one(next_five_indices):
                collections_of_straights.append(next_five_cards)

            index += 1

        return collections_of_straights

    @property
    def _dict_of_ranks_storing_lists_of_cards_of_the_same_rank(self):
        """
        example dictionary to build:
        {
            "2": [Card],
            "3": [Card],
            "4": [Card, Card],
            "5": [Card],
            "6": [Card, Card]
        }
        """

        cards_of_ranks_dict = {}

        for card in self.cards:
            if card.rank in cards_of_ranks_dict:
                cards_of_ranks_dict[card.rank].append(card)
            else:
                cards_of_ranks_dict[card.rank] = [card]

        return cards_of_ranks_dict

    @property
    def _list_containing_highest_valued_card_of_each_rank(self):
        # since the cards were appended as the higher value card of rank in the list, take last card for each rank
        return [
            cards[-1] for cards in self._dict_of_ranks_storing_lists_of_cards_of_the_same_rank.values()
        ]

    @property
    def _list_containing_five_consecutive_ordered_cards_of_same_suit(self):
        # returns a list of possible lists of 5 consecutive cards of the same rank, else return an empty list

        # extract the cards that have the same suit
        


        # straight_flush_cards = []
        # for card_list in self._collections_of_five_straight_cards_in_a_row:
        #     # use a set to remove any duplicates
        #     suits_seen = set()
        #     for card in card_list:
        #         suits_seen.add(card.suit)
        #     # if the suits_seen only contains one suit, then all cards passed in have the same suit
        #     if len(suits_seen) == 1:
        #         straight_flush_cards.append(card_list)
        #
        # return straight_flush_cards

    @property
    def _card_suit_counts(self):
        """ build dictionary to hold occurrences of cards suits seen """
        card_suit_counts = {}
        for card in self.cards:
            if card.suit in card_suit_counts:
                card_suit_counts[card.suit] += 1
            else:
                card_suit_counts[card.suit] = 1
        return card_suit_counts

    def _suits_with_counts(self, count):
        """ returns a dictionary with items that have a specified count """
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count == count
        }

    def _every_element_increasing_by_one(self, rank_indexes):
        # helper function to determine if card ranks are of consecutive order
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(range(starting_rank_index, last_rank_index + 1))
        return rank_indexes == straight_consecutive_indexes
