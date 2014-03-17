from strategies import Strategy
from helpers.cards import card_total


class HiLowCardCounter(Strategy):

	name = "HiLowCardCounter"

	# http://www.blackjackinfo.com/blackjack-school/blackjack-lesson-04.php
	pluses = ["2", "3", "4", "5", "6"]
	minuses = ["10", "J", "Q", "K", "A"]

	def hit_on(self, cards, remaining_cards, dealer_card):
		total = card_total(cards)

		# Always hit if we're too low
		if total <= 11:
			return True

		count = self.__card_count(remaining_cards)

		# Hit if the deck is stacked with low cards
		if total <= 15 and count > 0:
			return True

		return False

	def __card_count(self, cards):
		"""Total up a count for the remaining cards. A positive value means the
		deck is full of low cards while negative means there are lots of highs.
		"""
		count = 0

		for card in cards:
			if card.name in self.pluses:
				count += 1
			elif card.name in self.minuses:
				count -= 1

		return count
