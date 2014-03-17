from strategies.HitBelowStrategy import HitBelowStrategy
from models.Card import Card


def test_hits_below_limit():
	s = HitBelowStrategy(10)
	cards = [Card([1]), Card([1])]
	assert s.hit_on(cards, []) == True


def test_stays_above_limit():
	s = HitBelowStrategy(10)
	cards = [Card([6]), Card([6])]
	assert s.hit_on(cards, []) == False
