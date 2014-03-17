from nose.tools import raises

from models import Deck, Game
from strategies import Dealer, HitBelow


@raises(Exception)
def test_raises_with_no_dealer():
	gamblers = [HitBelow(1)]
	Game(None, gamblers, Deck)


@raises(Exception)
def test_raises_with_no_gamblers():
	Game(Dealer(), [], Deck)


@raises(Exception)
def test_raises_without_deck_factory():
	gamblers = [HitBelow(1)]
	Game(Dealer(), gamblers, None)
