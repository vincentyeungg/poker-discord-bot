class ValidatorHelpers:
    def __init__(self, cards):
        self.cards = cards

    @property
    def _card_rank_counts(self):
        """ build dictionary to hold occurrences of cards ranks seen to formulate best hand """
        card_rank_counts = {}
        for card in self.cards:
            if card.rank in card_rank_counts:
                card_rank_counts[card.rank] += 1
            else:
                card_rank_counts[card.rank] = 1
        return card_rank_counts

    def _ranks_with_counts(self, count):
        """ returns a dictionary with items that have a specified count """
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }
