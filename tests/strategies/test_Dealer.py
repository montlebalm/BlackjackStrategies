from strategies import Dealer
from models import Card


def test_hits_below_limit():
	s = Dealer()
	cards = [Card([16])]
	assert s.hit_on(cards, [], None) == True


def test_stays_at_limit():
	s = Dealer()
	cards = [Card([17])]
	assert s.hit_on(cards, [], None) == False


def test_stays_above_limit():
	s = Dealer()
	cards = [Card([17]), Card([1])]
	assert s.hit_on(cards, [], None) == False
