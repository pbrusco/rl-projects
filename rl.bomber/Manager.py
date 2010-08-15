#!/usr/local/bin/python
from Task import *
from StochasticNavigationTask import *
from StochasticExplosionTask import *
from TracingEnvironment import *
from Environment import *
from Agent import *
from Status import *
from RmaxAgent import *

import time
import pickle

AGENT_FILE_NAME = 'agent.pkl'
SAVE_EVERY = 10

class Manager:

	def __init__(self, iters=ITERATIONS, maxturns=MAX_TURNS):
		self.iters = iters
		self.maxturns = maxturns
		self.env = TracingEnvironment()
		self.task = Task(env=self.env)
		self.agent = RmaxAgent()

	def run(self):
		for r in range(self.iters):
			self.task.start()
			start = time.time()
			status = Status.CONTINUE
			state = self.task.getState()
			turn = 0
					
			# Run game for up to max turns 
			for turn in range(self.maxturns):
				action = self.agent.nextAction(state)
				nextstate,reward,status = self.task.perform(action)
				self.agent.learn(state,nextstate,action,reward)
				state = nextstate
				if status != Status.CONTINUE: break
			
			elapsed = time.time() - start
			if status == Status.CONTINUE and turn == self.maxturns-1: status = Status.TURNSUP
			self.reportgame(elapsed,turn,status)
			self.tryDumpGameTrace()
			
			# Dump the agent state every X iters
			if r > 0 and r % SAVE_EVERY == 0: self.saveAgent()
			
			
	def reportgame(self, elapsed, turns, status, ):
		print ' '.join([str(elapsed), str(turns), str(status)])
		
	def tryDumpGameTrace(self):
		try: self.env.dump()
		except Exception as e: print "Error dumping: ", e

	def saveAgent(self, agentName=AGENT_FILE_NAME):
		with open(agentName, 'wb') as output:
			pickle.dump(self.agent, output, -1)
			
	def loadAgent(self, agentName=AGENT_FILE_NAME):
		with open(agentName, 'rb') as input:
			self.agent = pickle.load(input)