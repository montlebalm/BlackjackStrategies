from models.Card import Card
from random import shuffle


class Deck(object):

	def __init__(self):
		suit = [
			Card(2, "2"),
			Card(3, "3"),
			Card(4, "4"),
			Card(5, "5"),
			Card(6, "6"),
			Card(7, "7"),
			Card(8, "8"),
			Card(9, "9"),
			Card(10, "10"),
			Card(10, "J"),
			Card(10, "K"),
			Card(10, "Q"),
			Card([11, 1], "A"),
		]

		self.cards = suit * 4

		# Shuffle the deck
		shuffle(self.cards)

	def get_next_card(self):
		return self.cards.pop()

	def next_card(self):
		return self.cards[-1]
