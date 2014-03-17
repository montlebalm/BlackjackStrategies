from strategies import Strategy
from helpers.cards import card_total


class Dealer(Strategy):

	name = "Dealer"

	def hit_on(self, cards, remaining_cards, dealer_card=None):
		return card_total(cards) < 17
