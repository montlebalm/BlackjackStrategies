from strategies import Strategy
from helpers.cards import card_total


class Psychic(Strategy):

	name = "Psychic"

	def hit_on(self, cards, remaining_cards, dealer_card):
		# Cheat by looking at the next card to see if we'll bust
		return card_total(cards + [remaining_cards[-1]]) <= 21
