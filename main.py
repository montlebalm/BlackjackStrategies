from models import Deck, Game
from strategies import Dealer, HitBelow, Psychic, HiLowCardCounter


def report(player, wins, rounds):
	pct = game.wins[player] * 100 // rounds
	print("%s: %d%%" % (player.name, pct))


if __name__ == "__main__":
	rounds = 10000
	dealer = Dealer()
	strats = [
		HitBelow(17),
		HiLowCardCounter(),
		Psychic(),
	]

	for strategy in strats:
		game = Game(dealer, strategy, Deck)

		for i in range(rounds):
			game.do_round()

		# Report
		report(dealer, game.wins[dealer], rounds)
		report(strategy, game.wins[strategy], rounds)
		print("")
