import random

class Deck(object):
	END_OF_DECK = -999
	def __init__(self):
		self.cards  =  ['A',2,3,4,5,6,7,8,9,10,'J','Q','K',
				'A',2,3,4,5,6,7,8,9,10,'J','Q','K',
				'A',2,3,4,5,6,7,8,9,10,'J','Q','K',
				'A',2,3,4,5,6,7,8,9,10,'J','Q','K']
	#Shuffle the Deck
	def reset(self):
		self.deck = self.cards
		random.shuffle(self.deck)
	
	def top(self):
		return self.deck[0]
	
	#Draw the top card
	def draw(self):
		if len(self.deck) < 1:
			return END_OF_DECK
		card = self.deck[0]
		self.deck = self.deck[1:]
		return card

	def get_ncards(self):
		return len(self.deck)