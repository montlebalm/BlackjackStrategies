from strategies import HiLowCardCounter
from models import Card


def test_hits_if_low_score():
	s = HiLowCardCounter()
	hole_cards = [Card(11)]
	assert s.hit_on(hole_cards, [], None) == True

def test_hits_if_high_score_and_low_deck():
	s = HiLowCardCounter()
	hole_cards = [Card(14)]
	remaining_cards = [Card(2, "2")]
	assert s.hit_on(hole_cards, remaining_cards, None) == True
