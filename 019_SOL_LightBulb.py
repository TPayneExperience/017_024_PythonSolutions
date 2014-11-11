#!/usr/bin/env python

from random import randint
from time import clock

## ===========================================
## STATES


class State(object):
	''' Base class for all inheriting subclasses '''
	pass

class LightOn(State):
	''' State in which Light is ON '''
	def Execute(self):
		print ("Light is ON")

class LightOff(State):
	''' State in which Light is OFF '''
	def Execute(self):
		print ("Light is OFF")

## ===========================================
## TRANSITION AND FSM

class Transition(object):
	''' Code executed when transitioning from one state to another '''
	def __init__(self, toState):
		self.toState = toState

	def Execute(self):
		print ("Transitioning...")

class SimpleFSM(object):
	''' A finite state machine that holds all states and transitions,
		as well as the current state and transition being executed.
		This is what will be executing the state and transition's functions.'''
	def __init__(self, char):
		self.char = char
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.trans = None

	def SetState(self, stateName):
		self.curState = self.states[stateName]

	def Transition(self, transName):
		self.trans = self.transitions[transName]

	def Execute(self):
		if (self.trans):
			self.trans.Execute()
			self.SetState(self.trans.toState)
			self.trans = None
		self.curState.Execute()

class Char(object):
	''' This is the character who will hold an instance of the FSM.'''
	def __init__(self):
		self.FSM = SimpleFSM(self)
		self.LightOn = True


## ===========================================
## TEST CODE

if __name__ == "__main__":
	light = Char()

	light.FSM.states["On"] = LightOn()
	light.FSM.states["Off"] = LightOff()
	light.FSM.transitions["toOn"] = Transition("On")
	light.FSM.transitions["toOff"] = Transition("Off")

	light.FSM.SetState("On")

	for i in range(20):
		startTime = clock()
		timeInterval = 1
		while (startTime + timeInterval > clock()):
			pass
		if (randint(0,2)):
			if (light.LightOn):
				light.FSM.Transition("toOff")
				light.LightOn = False
			else:
				light.FSM.Transition("toOn")
				light.LightOn = True
		light.FSM.Execute()