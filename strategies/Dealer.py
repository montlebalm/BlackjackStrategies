from strategies import Strategy
from helpers.cards import card_total


class Dealer(Strategy):

	name = "Dealer"

	def hit_on(self, cards, deck, dealer_card):
		return card_total(cards) < 17
