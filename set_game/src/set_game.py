import itertools
import random

class Card(object):

	@property
	def dimension_count(self): 	    # the dimension_count can be removed here, dimensions already contain the info
		return len(self.dimensions) # it can be passed in as a parameter in SampleGen(), don't have to a seperate attribute

	def __init__(self, card, dimension_count, dimension_size):
		self.dimensions = list(card)
		self.dimension_size = dimension_size


class Game(object):
	def __init__(self, cards, card_number):
		self.cards = cards
		self.card_number = card_number

	def solve(self):
		def set_checker(cards):
			for i in range(0, cards[0].dimension_size): # here should be dimension_size or dimension_count? can just do for i in range(dimension_count)
				to_check = [card.dimensions[i] for card in cards]
				if len(set(to_check)) == len(to_check) or len(set(to_check)) == 1:
					continue
				return False
			return True
		return [cards for cards in itertools.combinations(self.cards, self.card_number) if set_checker(self.cards)] # here I don't understand, set_checker should check each subset, why pass in self.cards here?
		

class SampleGen(object):
	def gen_sample_cards(self, total_cards_count, dimensions_count, size, card_count):
		def gen_sample():
			result = []
			for i in range(0, dimensions_count):
				result.append(random.randint(0, size))
			return result
		return [gen_sample() for _ in range(card_count)] # what is card_count? shall it be total_cards_count?, card_count here is not needed

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
