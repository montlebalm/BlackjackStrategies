from strategies import Strategy
from helpers.cards import card_total


class HitBelow(Strategy):

	name = "HitBelow"

	def __init__(self, limit):
		self.limit = limit
		self.name += str(limit)

	def hit_on(self, cards, remaining_cards, dealer_card):
		return card_total(cards) < self.limit
