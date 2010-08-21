from Task import *
from TracingEnvironment import *
from Environment import *
from Status import *
from Settings import *
from Constants import *
from copy import copy, deepcopy

import Factory
import time
import pickle

AGENT_FILE_NAME = 'agent.pkl'
SAVE_EVERY = 100

class Manager:

	def __init__(self, iters=ITERATIONS, maxturns=MAX_TURNS):
		self.iters = iters
		self.maxturns = maxturns
		env = TracingEnvironment()
		self.task = Factory.createTask(env)
		self.agent = Factory.createAgent()

	def run(self):
		for r in range(self.iters):
			self.task.start()
			start = time.time()
			status = Status.CONTINUE
			state = self.task.getState()
			state = deepcopy(state) if AGENT in FACTOREDAGENTS else int(state)
			
			turn = 0
			totalMovementActionsCount = 0
			totalDropActionCount = 0
			totalExplodeActionCount = 0
			noResultActionsCount = 0

			action = self.agent.nextAction(state)
			
			# Run game for up to max turns 
			for turn in range(self.maxturns):
				
				if (Action.isNavigationAction(action)):
					totalMovementActionsCount +=1
				elif (action == Action.DROP_BOMB):
					totalDropActionCount +=1
				else:
					totalExplodeActionCount +=1
					
				# Have the agent choose next action
				nextstate,reward,status = self.task.perform(action)
				#print reward
				
				# Convert state and reward to factored if necessary or encode otherwise
				if AGENT in FACTOREDAGENTS: nextstate, reward = deepcopy(nextstate), deepcopy(reward)
				else: nextstate, reward = int(nextstate), float(reward)
				
				nextChosenAction = self.agent.nextAction(nextstate) if AGENT in REQUIRESNEXTACTION else None
				
				# Agent learns from action
				self.agent.learn(state,nextstate,action,reward,nextChosenAction)
				
				if (nextstate == state):
					noResultActionsCount +=1
				
				state = nextstate
				action = nextChosenAction if AGENT in REQUIRESNEXTACTION else self.agent.nextAction(state)
				
				if status != Status.CONTINUE: break
			
			elapsed = time.time() - start
			if status == Status.CONTINUE and turn == self.maxturns-1: status = Status.TURNSUP
			self.reportgame(elapsed,turn,status,totalMovementActionsCount,totalDropActionCount,totalExplodeActionCount,noResultActionsCount)
			self.tryDumpGameTrace()
			
			# Dump the agent state every X iters
			if SAVE_EVERY > 0 and r > 0 and r % SAVE_EVERY == 0: self.saveAgent()
			
	def reportgame(self, elapsed, turns, status,totalMovementActionsCount, totalDropActionCount, totalExplodeActionCount, noResultActionsCount, ):
		print '	'.join([str(elapsed), str(turns), str(status), str(totalMovementActionsCount), str(totalDropActionCount), str(totalExplodeActionCount), str(noResultActionsCount) ])
		
	def tryDumpGameTrace(self):
		try: self.task.env.dump()
		except Exception as e: print "Error dumping: ", e

	def saveAgent(self, agentName=AGENT_FILE_NAME):
		agentName = "Output/" + CONFIGURATION_NAME + "-" + agentName
		with open(agentName, 'wb') as output:
			pickle.dump(self.agent, output, -1)
			
	def loadAgent(self, agentName=AGENT_FILE_NAME):
		agentName = "Output/" + CONFIGURATION_NAME + "-" + agentName
		with open(agentName, 'rb') as input:
			self.agent = pickle.load(input)

	def see(self):
		return self.loadAndInspectLastSavedAgent()
	
	def loadAndInspectLastSavedAgent(self):
		self.loadAgent()
		print self.agent.inspect()