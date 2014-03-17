from models.Deck import Deck
from models.Game import Game
from strategies.DealerStrategy import DealerStrategy
from strategies.HitBelowStrategy import HitBelowStrategy
from strategies.PsychicStrategy import PsychicStrategy


if __name__ == "__main__":
	rounds = 1000
	strats = [
		HitBelowStrategy(1),
		PsychicStrategy()
	]

	for strategy in strats:
		dealer = DealerStrategy()
		gamblers = [strategy]
		game = Game(dealer, gamblers, Deck)
		wins = {p: 0 for p in [dealer] + gamblers}

		# Run the game for n turns
		for i in range(rounds):
			outcome = game.do_round()
			scores = outcome[0]
			winner = outcome[1]

			# Record the win
			wins[winner] += 1

		for player in wins:
			pct = wins[player] * 100 // rounds
			print(player.name + ": " + str(wins[player]) + " (" + str(pct) + "%)")

		print("")

