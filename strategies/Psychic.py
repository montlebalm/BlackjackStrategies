from strategies import Strategy
from helpers.cards import card_total


class Psychic(Strategy):

	name = "Psychic"

	def hit_on(self, cards, deck, dealer_card):
		# Cheat by looking at the next card to see if we'll bust
		return card_total(cards + [deck.next_card()]) <= 21
