import random
from deck import Deck
from player import Player
class BlackJack(object):
	END_OF_DECK = -999

	def __init__(self):
		self.deck = Deck()
		self.deck.reset()
		self.open_26 = 0
		self.open_79 = 0
		self.open_10 = 0
		self.open_Ace = 0	
		self.wager = 0
		self.in_play = False
		#self.end = False


	# Resets Player and Dealer. DOES NOT SHUFFLE DECK
	# 0 Reward
	def start(self,b):
		#Player bets sum b
		self.in_play = True
		self.wager = b
		self.player = Player()
		self.dealer = Player()
		self.ppts = 0
		self.dpts = 0
		self.player.bet(b,self.deck)

		#Dealer draws one card, player 2
		r = self.dealer.draw(self.deck)
		if r == -999:
			return r
		open_cards = self.player.get_hand() + self.dealer.get_hand()
		for card in open_cards:
			if card == 'A':
				self.open_Ace += 1
			if card in ['K','Q','J',10]:
				self.open_10 += 1
			if card in [2,3,4,5,6]:
				self.open_26 += 1
			if card in [7,8,9]:
				self.open_79 += 1
		self.ppts = self.player.get_points()
		self.dpts = self.dealer.get_points()
		return (self.open_Ace,self.open_26,self.open_79,self.open_10,self.ppts,self.dpts,0)
	
	#Update player and game state
	def hit(self):
		#Player chooses to draw a card
		reward = 0
		card = self.player.draw(self.deck)
		if card == -999:
			return card
		if card == 'A':
			self.open_Ace += 1
		if card in ['K','Q','J',10]:
			self.open_10 += 1
		if card in [2,3,4,5,6]:
			self.open_26 += 1
		if card in [7,8,9]:
			self.open_79 += 1
		self.ppts = self.player.get_points()
		if self.ppts > 21:
			#Game Ends
			reward = -1*self.wager
			self.in_play = False
		self.dpts = self.dealer.get_points()
		return (self.open_Ace,self.open_26,self.open_79,self.open_10,self.ppts,self.dpts,reward)
	
	def stand(self):
		#Player chooses to stop
		reward = self.wager
		
		#Dealer draws till his points reach more than 17
		while self.dealer.get_points() < 17:
			card = self.dealer.draw(self.deck)
			if card == -999:
				return card
			if card == 'A':
				self.open_Ace += 1
			if card in ['K','Q','J',10]:
				self.open_10 += 1
			if card in [2,3,4,5,6]:
				self.open_26 += 1
			if card in [7,8,9]:
				self.open_79 += 1
			

		self.dpts = self.dealer.get_points()

		if self.ppts > 21:
			#Player Loses
			reward = -1*reward
			self.in_play = False
		else :
			if self.dpts > 21:
				#House loses				
				reward = 2*reward
				self.in_play = False
			else:
				if self.ppts > self.dpts:
					#Player Wins
					reward = 2*reward
					self.in_play = False
				else:
					if self.ppts < self.dpts:
						#House Wins
						reward = -1*reward
						self.in_play = False
					else:
						#Tie
						self.in_play = False
		return (self.open_Ace,self.open_26,self.open_79,self.open_10,self.ppts,self.dpts,reward)	