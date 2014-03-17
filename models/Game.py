from helpers.cards import card_total


class Game(object):

	def __init__(self, dealer, gamblers, deck_factory):
		if dealer is None:
			raise Exception("You must have a dealer")

		if len(gamblers) == 0:
			raise Exception("You must have some gamblers")

		if deck_factory is None:
			raise Exception("You must have a deck factory")

		self.__dealer = dealer
		self.__gamblers = gamblers
		self.__players = [self.__dealer] + gamblers
		self.__deck_factory = deck_factory
		self.__deck = self.__deck_factory()
		self.wins = {p: 0 for p in self.__players}

	def do_round(self):
		"""Play a round of Blackjack with all players
		"""
		# Get every player's cards first
		cards = {p: self.__get_cards_from_deck(2) for p in self.__players}
		# Let each player hit and then total up the scores
		scores = {p: self.__get_player_total(p, cards[p]) for p in self.__players}
		winner = self.__get_winner(scores)
		self.wins[winner] += 1

		return (scores, winner)

	def __get_cards_from_deck(self, num_cards):
		"""Get n number of cards from the deck
		"""
		cards = []

		for i in range(num_cards):
			if len(self.__deck.cards) == 0:
				self.__deck = self.__deck_factory()
			cards.append(self.__deck.get_next_card())

		return cards

	def __get_player_total(self, player, cards):
		"""Employ the player's strategy to get the highest hand score
		"""
		# Let players hit until they're satisfied or they bust
		while card_total(cards) <= 21:
			# Make sure we have cards left in the deck
			if len(self.__deck.cards) == 0:
				self.__deck = self.__deck_factory()

			if player.hit_on(cards, self.__deck):
				cards += self.__get_cards_from_deck(1)
			else:
				break

		return card_total(cards)

	def __get_winner(self, scores):
		"""Figure out which player won based on the scores
		"""
		# Strip out all the gamblers that busted
		unbusted_gamblers = [p for p in self.__gamblers if scores[p] <= 21]
		# Sort the gamblers by card value
		sorted(unbusted_gamblers, key=lambda p: scores[p])

		if len(unbusted_gamblers) > 0:
			best_gambler = unbusted_gamblers[-1]
			dealer_busted = scores[self.__dealer] > 21

			# The best gambler wins if the dealer busts or he beats him
			if dealer_busted or scores[best_gambler] > scores[self.__dealer]:
				return best_gambler

		return self.__dealer
