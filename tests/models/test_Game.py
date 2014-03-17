from nose.tools import raises

from models.Deck import Deck
from models.Game import Game
from strategies.DealerStrategy import DealerStrategy
from strategies.HitBelowStrategy import HitBelowStrategy


@raises(Exception)
def test_raises_with_no_dealer():
	gamblers = [HitBelowStrategy(1)]
	Game(None, gamblers, Deck)


@raises(Exception)
def test_raises_with_no_gamblers():
	Game(DealerStrategy(), [], Deck)


@raises(Exception)
def test_raises_without_deck_factory():
	gamblers = [HitBelowStrategy(1)]
	Game(DealerStrategy(), gamblers, None)
