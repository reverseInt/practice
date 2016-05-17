import itertools
import random

class Card(object):

	@property
	def dimensions(self):
		return self._dimensions

	@property
	def dimension_count(self):
		return len(self.dimensions)

	@property
	def dimension_size(self):
		return self._dimension_size

	def __init__(self, card, dimension_count, dimension_size):
		self._dimensions = list(card)
		self._dimension_size = dimension_size


class Game(object):
	def __init__(self, cards, card_number):
		self.cards = cards
		self.card_number = card_number

	def solve(self):
		def set_checker(cards):
			for i in range(0, cards[0].dimension_size):
				to_check = [card.dimensions[i] for card in cards]
				if len(set(to_check)) == len(to_check) or len(set(to_check)) == 1:
					continue
				return False
			return True
		return [cards for cards in itertools.combinations(self.cards, self.card_number) if set_checker(self.cards)]
		

class SampleGen(object):
	def gen_sample_cards(self, total_cards_count, dimensions_count, size, card_count):
		def gen_sample():
			result = []
			for i in range(0, dimensions_count):
				result.append(random.randint(0, size))
			return result
		return [perm for perm in [gen_sample() for _ in range(card_count)]]

if __name__ == '__main__':
	total_cards_count = 9
	dimensions_count = 4
	dimensions_size = 4
	card_count = 3

	cards = [Card(gen, dimensions_count, dimensions_size) for gen in [[1,0,0,1], [0,0,0,2], [2,0,0,0]]]
	s = SampleGen()
	#cards = [Card(gen, dimensions_count, dimensions_size) for gen in s.gen_sample_cards(total_cards_count, dimensions_count, dimensions_size, card_count)]
	g = Game(cards, card_count)
	for cards in g.solve():
		print 'output:', [card.dimensions for card in cards]
