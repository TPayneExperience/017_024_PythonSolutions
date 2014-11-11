#!usr/bin/env python

try:
	from Queue import PriorityQueue
except:
	from queue import PriorityQueue


class State(object):
	''' Base template class to be inherited from for subclasses '''
	def __init__(self, value, parent,
                     start = 0, goal = 0):
		''' Constructor that stores parent, value, start and goal '''
		self.children = []
		self.parent = parent
		self.value = value
		self.dist = 0
		if parent:
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal
		else:
			self.path = [value]
			self.start = start
			self.goal = goal

	def GetDist(self):
		pass
	def CreateChildren(self):
		pass


class State_String(State):
	def __init__(self, value, parent, start = 0, 
					goal = 0):
		super(State_String, self).__init__(value, 
			parent, start, goal)
		self.dist = self.GetDist()
	
	def GetDist(self):
		''' Get the current distance to goal, 
			which will be state's value '''
		if self.value == self.goal:
			return 0
		dist = 0
		for i in range(len(self.goal)):
			letter = self.goal[i]
			dist += abs(i - self.value.index(letter))
		return dist

	def CreateChildren(self):
		''' Generate all possible children,
			by switching two adjacent letters around '''
		if not self.children:
			for i in range(len(self.goal)-1):
				val = self.value
				val = val[:i] + val[i+1] + val[i] + val[i+2:]
				child = State_String(val, self)
				self.children.append(child)


class AStar_Solver:
	def __init__(self, start, goal):
		''' Store the start and goal of program, and set up vars '''
		self.path = []
		self.visitedQueue = []
		self.priorityQueue = PriorityQueue()
		self.start = start
		self.goal = goal

	def Solve(self):
		''' Create start state, then organize children 
		based on value and check children of highest value child '''
		startState = State_String(self.start, 
									0, 
									self.start, 
									self.goal)
		count = 0
		self.priorityQueue.put((0, count, startState))
		while(not self.path and self.priorityQueue.qsize()):
			closestChild = self.priorityQueue.get()[2]
			closestChild.CreateChildren()
			self.visitedQueue.append(closestChild.value)
			for child in closestChild.children:
				if child.value not in self.visitedQueue:
					count += 1
					if not child.dist:
						self.path = child.path
						break
					self.priorityQueue.put((child.dist, count, child))
		if not self.path:
			print ("Goal of " + self.goal + " is not possible!")
		return self.path
				

##=======================================
## MAIN

if __name__ == "__main__":
	start1 = "nra sdfasd Fevev."
	goal1 = "Fd.safdsa ev evnr"
	print ('starting...')
	a = AStar_Solver (start1, goal1)
	a.Solve()
	for i in range(len(a.path)):
		print ("%d) " %i + a.path[i])
