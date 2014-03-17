from strategies import HitBelow
from models import Card


def test_hits_below_limit():
	s = HitBelow(10)
	cards = [Card([1]), Card([1])]
	assert s.hit_on(cards, [], None) == True


def test_stays_above_limit():
	s = HitBelow(10)
	cards = [Card([6]), Card([6])]
	assert s.hit_on(cards, [], None) == False
