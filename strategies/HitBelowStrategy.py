from strategies.Strategy import Strategy
from helpers.cards import card_total


class HitBelowStrategy(Strategy):

	name = "HitBelow"

	def __init__(self, limit):
		self.limit = limit
		self.name += str(limit)

	def hit_on(self, cards, deck):
		return card_total(cards) < self.limit
