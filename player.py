from deck import Deck

class Player(object):
	def __init__(self):
		self.cash = 10
		self.hand = []
		self.points = 0
		self.nAces = 0

	#Starting wager, draw two cards
	def bet(self,b,deck):
		self.cash -= b
		self.draw(deck)
		r = self.draw(deck)
		return r
	
	#Update your hand on draw
	def draw(self,deck):
		card = deck.draw()
		self.hand.append(card)
		self.calculate_points()
		return card
	
	def calculate_points(self):
		points = 0
		aces = 0
		for card in self.hand:
			if card == 'A':
				aces += 1
				points += 11
			if card in ['K','Q','J']:
				points += 10 #Face Card Value = 10
			if card in [2,3,4,5,6,7,8,9,10] :
				points += card #2-10 have corresponding values
			while points > 21 and aces > 0:
				#Aces can take 1 or 11 values
				points -= 10
				aces -= 1
		self.points = points
	def get_points(self):
		return self.points
	def get_hand(self):
		return self.hand