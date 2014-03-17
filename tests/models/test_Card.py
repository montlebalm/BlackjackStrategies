from models.Card import Card


def test_stores_values_as_list():
	c = Card(1, "Test")
	assert c.values.pop
