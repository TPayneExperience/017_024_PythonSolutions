#!/usr/bin/env python

import re, urllib, threading, time

try:
	import urllib.request
except:
	pass

def GetNameFromURL(website, pattern, *args, **kwargs):
	start = time.clock()
	try:
		u = urllib.urlopen('http://' + website + '.com')
	except:
		u = urllib.request.urlopen('http://' + website + '.com')
	text = u.read()
	title = re.findall(pattern, str(text))
	print ("Completed " + title[0] + " in " + str(time.clock()-start))


if __name__ == '__main__':
	sites = 'google yahoo cnn msn'.split()

	## -- EASY --
	pattern = re.compile(r'<title>+(.*)</title>+', re.I|re.M) 

	threadList = []
	for s in sites:
		print ('Searching: ' + s)
		t = threading.Thread(target=GetNameFromURL, 
						args=(s, pattern))
		t.start()
		threadList.append(t)
	print ('\nMAIN PROGRAM COMPLETE\n')


		
