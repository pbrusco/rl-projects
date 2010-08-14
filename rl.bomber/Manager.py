#!/usr/local/bin/python
from Task import Task
from Environment import *
from Agent import *
from Status import *

import time

class Manager:

	def __init__(self, iters=ITERATIONS, maxturns=MAX_TURNS):
		self.iters = iters
		self.maxturns = maxturns
		self.env = Environment()
		self.task = Task(env=self.env)
		self.agent = Agent()

	def run(self):
		for r in range(self.iters):
			self.task.start()
			start = time.time()
			status = Status.CONTINUE
			state = self.task.getState()
			turn = 0
			
			for turn in range(self.maxturns):
				action = self.agent.nextAction(state)
				nextstate,reward,status = self.task.perform(action)
				self.agent.learn(state,nextstate,action,reward)
				state = nextstate
				if status != Status.CONTINUE: break
			
			elapsed = time.time() - start
			if status == Status.CONTINUE and turn == self.maxturns-1: status = Status.TURNSUP
			self.reportgame(elapsed,turn,status)
			
	def reportgame(self, elapsed, turns, status):
		print ' '.join([str(elapsed), str(turns), str(status)])
