class Card(object):

	def __init__(self, values, name=""):
		self.name = name

		try:
			# Try to treat the value as a list first
			self.values = list(values)
		except:
			self.values = [values]
