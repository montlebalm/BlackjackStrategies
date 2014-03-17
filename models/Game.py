from helpers.cards import card_total


class Game(object):

	def __init__(self, dealer, gambler, deck_factory):
		if dealer is None:
			raise Exception("You must have a dealer")

		if gambler is None:
			raise Exception("You must have a gambler")

		if deck_factory is None:
			raise Exception("You must have a deck factory")

		self.__dealer = dealer
		self.__player = gambler
		self.__players = [self.__dealer, gambler]
		self.__deck_factory = deck_factory
		self.__deck = None
		self.wins = {p: 0 for p in self.__players}

	def do_round(self):
		"""Play a round of Blackjack with all players
		"""
		# Get every player's cards first
		hole_cards = {p: list(self.__next_cards(2)) for p in self.__players}
		dealer_card = hole_cards[self.__dealer][0]

		# Let players hit until they're satisfied
		final_cards = {p: self.__player_turn(p, hole_cards[p], dealer_card) for p in hole_cards}

		# Figure out who won
		winner = self.__get_winner(final_cards)

		if winner is not None:
			self.wins[winner] += 1

	def __next_cards(self, count):
		"""Get n number of cards from the deck
		"""
		for i in range(count):
			# Make sure we have a deck with enough cards
			if self.__deck is None or len(self.__deck.cards) == 0:
				self.__deck = self.__deck_factory()

			yield self.__deck.get_next_card()

	def __player_turn(self, player, hole_cards, dealer_card):
		"""Employ the player's strategy to get the highest hand score
		"""
		cards = hole_cards[:]

		# Let players hit until they're satisfied or they bust
		while card_total(cards) < 21:
			# Make sure we have cards left in the deck
			if not self.__deck.cards:
				self.__deck = self.__deck_factory()

			if player.hit_on(cards, self.__deck.cards, dealer_card):
				cards += self.__next_cards(1)
			else:
				break

		return cards

	def __get_winner(self, player_cards):
		"""Figure out who won based on the hands
		"""
		player_score = card_total(player_cards[self.__player])
		player_count = len(player_cards[self.__player])
		dealer_score = card_total(player_cards[self.__dealer])
		dealer_count = len(player_cards[self.__dealer])

		# Check who busted
		if dealer_score > 21 and player_score > 21:
			return None
		elif player_score > 21:
			return self.__dealer
		elif dealer_score > 21:
			return self.__player

		player_blackjack = player_score == 21 and player_count == 2
		dealer_blackjack = dealer_score == 21 and dealer_count == 2

		# Check for blackjacks
		if dealer_blackjack and player_blackjack:
			return None
		elif player_blackjack:
			return self.__player
		elif dealer_blackjack:
			return self.__dealer

		# Check "5-card rule"
		if dealer_count >= 5 and player_count >= 5:
			return None
		elif player_count >= 5:
			return self.__player
		elif dealer_count >= 5:
			return self.__dealer

		# Check point values
		if player_score == dealer_score:
			return None
		if player_score > dealer_score:
			return self.__player
		elif dealer_score > player_score:
			return self.__dealer
