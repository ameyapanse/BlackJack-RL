from game import BlackJack

# Action Encodings
# Hit = 1
# Stand = 0

# 1 : High Wager
# 2 : Low Wager

Q_dic = {}
#Q_dic[oA,o26,o79,o10,ppt,dpt,action] = action value


def get_Q(sa):
	global Q_dic
	if sa in Q_dic:
		return Q_dic[sa]
	return 0


alpha = 0.7
gamma = 0.8
epsilon = 0.2


def Q_update(state_action,reward,next_state):
	global Q_dic
	cval = get_Q(state_action)
	next_action = policy(next_state)
	opt_up = reward + gamma*get_Q(next_state+(next_action,)) - cval
	Q_dic[state_action] = cval + alpha*opt_up
	#print state_action,reward,next_state
	return Q_dic[state_action]


def policy(state,exploit = False):
	if not exploit and random.random < epsilon:
		if random.random < 0.5:
			return 0
		return 1
	if get_Q(state+(0,)) == get_Q(state+(1,)):
		if random.random < 0.5:
			return 0
		return 1
	if get_Q(state+(0,)) > get_Q(state+(1,)):	
		return 0
	return 1


def learn(max_iter=10):
	i=0
	M = 500
	B = BlackJack()
	state = (0,0,0,0,0,0)
	rews = []
	while i < max_iter:

		action = policy(state)
		#Get the Action

		
		if state[-1] == 0:
			#Place High/Low Wager
			ret = B.start(action*4 + 1)
		else:
			#Hit/Stand
			if action == 0:
				ret = B.stand()
			else :
				ret = B.hit()

		if ret == -999:
			#Restart. Deck has ended
			state = (0,0,0,0,0,0)
			B = BlackJack()
			continue
		
		nstate = ret[:-1]

		if not B.in_play:
			#Reset player/dealer current points
			nstate = nstate[:-2] + (0,0)

		reward = ret[-1]
		rews.append(ret)
		#Update Q Values
		Q_update(state + (action,),reward,nstate)
		state = nstate
		i+=1
	#return rews

'''
def test(nruns)	
	i=0
	wager_reward = []
	while(i<nruns):
		#Play Games till end of deck. Give reward
		B = BlackJack()
		state = (0,0,0,0,0,0)
		action = policy(state,True)
		s = B.start(action*4 + 1)
		reward += s[-1]
		state = s[:-1]
		while B.in_play:
			
			action = policy(state)
'''