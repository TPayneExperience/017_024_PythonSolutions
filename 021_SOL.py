#!/usr/bin/env python

from sys import maxsize

##===========================================================================
## TREE BUILDER
class Node(object):
	''' An object used to determine the depth, playerNumber and 
		value of the current state of the game'''
	def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value = 0):
		self.i_depth = i_depth
		self.i_playerNum = i_playerNum
		self.i_sticksRemaining = i_sticksRemaining
		self.i_value = i_value
		self.children = []
		self.CreateChildren()

	def CreateChildren(self):
		''' Creates the possible choices for the current Node '''
		if self.i_depth >= 0:
			for i in range(1, 4): # -- MEDIUM ---
				v = self.i_sticksRemaining - i
				self.children.append( Node( self.i_depth - 1, 
											-self.i_playerNum, 
											v, 
											self.RealVal(v)))

	def RealVal(self, value):
		''' Determines value to player based on if is last stick or not '''
		if (value == 0):
			return maxsize * self.i_playerNum
		elif (value < 0):
			return maxsize * -self.i_playerNum
		return 0


##==========================================================
## ALGORHITHM
def MinMax(node, i_depth, i_playerNum):
	''' Determines best choice available for current player '''
	if (i_depth == 0) or (abs(node.i_value) == maxsize):
		return node.i_value
	
	i_bestValue = maxsize * -i_playerNum

	for i in range(len(node.children)):
		child = node.children[i]
		i_val = MinMax(child, i_depth - 1, -i_playerNum)
		if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
			i_bestValue = i_val
			if abs(i_bestValue) == maxsize: ## -- HARD --
				break
	return i_bestValue

##==========================================================
## IMPLEMENTATION
def WinCheck(i_sticks, i_playerNum):
	''' Check to see if a player has won. '''
	if i_sticks <= 0:
		print ("*"*30)
		if i_playerNum > 0:
			if i_sticks == 0:
				print ("\tYou WIN!!!")
			else:
				print ("\tTOO MANY! You lose...")
		else:
			if i_sticks == 0:
				print ("\tComp Wins... Better luck next time.")
			else:
				print ("\tCOMP ERROR!")
		print ("*"*30)
		return 0
	return 1


##==========================================================
## TEST

if __name__ == '__main__':
	i_stickTotal = 11
	i_depth = 4
	i_curPlayer = 1
	print ("""INSTRUCTIONS: Be the player to pick up the last stick
\t\tYou can only pick up only pick up one (1), two (2)
\t\t OR three (3)sticks at at time.""")
	while (i_stickTotal > 0):
		print ("\n%d sticks remain. How many would you like to pick up?" %i_stickTotal)
		i_choice = input("\n1, 2 or 3: ") # -- MEDIUM ---
		i_stickTotal -= int(float(i_choice))
		if WinCheck(i_stickTotal, i_curPlayer):
			i_curPlayer *= -1
			node = Node(i_depth, i_curPlayer, i_stickTotal)
			bestChoice = -100
			i_bestValue= -i_curPlayer * maxsize

			## DETERMINE NUMBER OF STICKS TO REMOVE
			for i in range(len(node.children)):
				n_child = node.children[i]
				i_val = MinMax(n_child, i_depth, -i_curPlayer)
				if (abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_bestValue)):
					i_bestValue = i_val
					bestChoice = i

			bestChoice += 1
			print ("Comp chooses: " + str(bestChoice) + "\tBased on value: " + str(i_bestValue))
			i_stickTotal -= bestChoice
			WinCheck(i_stickTotal, i_curPlayer)
			i_curPlayer *= -1
