#!/usr/bin/env python

import threading, random, time

lock = threading.Lock() # -- HARD --

def Splitter(words):
	global lock # -- HARD --
	mylist = words.split()
	newList = []

	while (mylist):
		newList.append(mylist.pop(
			random.randrange(0, len(mylist))))
	time.sleep(1) 

	# with lock: ## -- HARD -- ## forces ONLY ONE thread at a time, Halts others
	# 	while (mylist):
	# 		newList.append(mylist.pop(
	# 			random.randrange(0, len(mylist))))
	# 	time.sleep(1) 

	print (' '.join(newList))


if __name__ == '__main__':
	sentance = 'I am a handsome beast. Word.'
	numOfThreads = 5
	threadList = []

	print ("STARTING...\n")
	start = time.clock()
	for i in range(numOfThreads):
		t = threading.Thread(target=Splitter, 
						args=(sentance,))
		t.start()
		threadList.append(t)
		# t.join() ## Forces MAIN program to WAIT until thread finished
	print ("\nThread Count: " + 
		str(threading.activeCount()))
	finish = time.clock()
	MTT = finish - start
	
	# -- MEDIUM --
	# SINGLE THREAD 
	# start = time.clock()
	# for i in range(numOfThreads):
	# 	mylist = sentance.split()
	# 	newList = []
	# 	while (mylist):
	# 		newList.append(mylist.pop(
	# 			random.randrange(0, len(mylist))))
	# 	print (' '.join(newList))
	
	# finish = time.clock()
	# print ('SINGLETHREAD TOTAL TIME: ' + str(finish - start))
	print ('MULTITHREAD TOTAL TIME: ' + str(MTT))


	print ("EXITING...\n")