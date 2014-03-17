from strategies.DealerStrategy import DealerStrategy
from models.Card import Card


def test_hits_below_limit():
	s = DealerStrategy()
	cards = [Card([s.limit - 1])]
	assert s.hit_on(cards, []) == True


def test_stays_at_limit():
	s = DealerStrategy()
	cards = [Card([s.limit])]
	assert s.hit_on(cards, []) == False


def test_stays_above_limit():
	s = DealerStrategy()
	cards = [Card([s.limit]), Card([1])]
	assert s.hit_on(cards, []) == False
