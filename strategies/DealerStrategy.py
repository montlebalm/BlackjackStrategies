from strategies.Strategy import Strategy
from helpers.cards import card_total


class DealerStrategy(Strategy):

	name = "Dealer"
	limit = 17

	def hit_on(self, cards, deck):
		return card_total(cards) < self.limit
