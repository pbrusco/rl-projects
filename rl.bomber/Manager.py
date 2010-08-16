from Task import *
from TracingEnvironment import *
from Environment import *
from Agent import *
from Status import *
from Settings import *

import Factory
import time
import pickle

AGENT_FILE_NAME = 'qagent.pkl'
SAVE_EVERY = 0

class Manager:

	def __init__(self, iters=ITERATIONS, maxturns=MAX_TURNS):
		self.iters = iters
		self.maxturns = maxturns
		self.env = TracingEnvironment()
		self.task = Factory.createTask()
		self.agent = Factory.createAgent()

	def run(self):
		for r in range(self.iters):
			self.task.start()
			start = time.time()
			status = Status.CONTINUE
			state = self.task.getState()
			turn = 0
			totalMovementActionsCount = 0
			totalDropActionCount = 0
			totalExplodeActionCount = 0
			
			noResultActionsCount = 0
			
					
			# Run game for up to max turns 
			for turn in range(self.maxturns):
				action = self.agent.nextAction(state)
				if (action < 4):
					totalMovementActionsCount +=1
				elif (action == 4):
					totalDropActionCount +=1
				else:
					totalExplodeActionCount +=1
					
				nextstate,reward,status = self.task.perform(action)
				self.agent.learn(state,nextstate,action,reward)
				if (state == nextstate):
					noResultActionsCount +=1
				state = nextstate
				if status != Status.CONTINUE: break
			
			elapsed = time.time() - start
			if status == Status.CONTINUE and turn == self.maxturns-1: status = Status.TURNSUP
			self.reportgame(elapsed,turn,status,totalMovementActionsCount,totalDropActionCount,totalExplodeActionCount,noResultActionsCount)
			self.tryDumpGameTrace()
			
			# Dump the agent state every X iters
			if SAVE_EVERY > 0 and r > 0 and r % SAVE_EVERY == 0: self.saveAgent()
			
			
	def reportgame(self, elapsed, turns, status,totalMovementActionsCount, totalDropActionCount, totalExplodeActionCount, noResultActionsCount, ):
		print ' '.join([str(elapsed), str(turns), str(status), str(totalMovementActionsCount), str(totalDropActionCount), str(totalExplodeActionCount), str(noResultActionsCount) ])
		
	def tryDumpGameTrace(self):
		try: self.env.dump()
		except Exception as e: print "Error dumping: ", e

	def saveAgent(self, agentName=AGENT_FILE_NAME):
		with open(agentName, 'wb') as output:
			pickle.dump(self.agent, output, -1)
			
	def loadAgent(self, agentName=AGENT_FILE_NAME):
		with open(agentName, 'rb') as input:
			self.agent = pickle.load(input)

	def see(self):
		return self.loadAndInspectLastSavedAgent()
	
	def loadAndInspectLastSavedAgent(self):
		self.loadAgent()
		print self.agent.inspect()