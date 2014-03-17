class Strategy(object):

	name = "None"

	def hit_on(self, cards, remaining_cards, dealer_card):
		raise

	def __str__(self):
		return self.name
