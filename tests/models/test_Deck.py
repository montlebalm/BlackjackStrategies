from models.Deck import Deck


def test_contains_52_cards():
	d = Deck()
	assert len(d.cards) == 52


def test_cards_are_shuffled():
	d1 = Deck()
	d2 = Deck()
	# Find all the indexes where cards from d1 and d2 are identical
	dupes = [c.values == d2.cards[i] for i, c in enumerate(d1.cards)]
	# all() should return False if any of the indexes didn't match
	assert all(dupes) == False


def test_contains_4_of_each_card():
	d = Deck()
	counts = {c.name: 0 for c in d.cards}

	for card in d.cards:
		counts[card.name] += 1

	for name in counts:
		assert counts[name] == 4


def test_returns_next_card():
	d = Deck()
	assert d.next_card() == d.get_next_card()
