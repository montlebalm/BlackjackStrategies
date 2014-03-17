from strategies import Psychic
from models import Card


def test_hits_if_wont_bust():
	s = Psychic()
	cards = [Card([19])]
	assert s.hit_on(cards, [Card(2)], None) == True


def test_stays_if_will_bust():
	s = Psychic()
	cards = [Card([20])]
	assert s.hit_on(cards, [Card(2)], None) == False
