#!/usr/bin/env python

BaseClass = type("BaseClass", (object,), {})

# -- 2 ---
BaseClass2 = type("BaseClass2", (object,), {})

@classmethod
def Check1(self, myStr):
	return myStr == "ham"

@classmethod
def Check2(self, myStr):
	return myStr == "sandwich"

# -- 1 --
@classmethod
def Check3(self, myStr):
	return myStr == "pancakes"

C1 = type("C1", (BaseClass,), {"x": 1, "Check": Check1})
C2 = type("C2", (BaseClass, BaseClass2), {"x": 30, "Check": Check2})
C3 = type("C3", (BaseClass, BaseClass2), {"x": 45, "Check": Check3})

def MyFactor(myStr):
	for cls in BaseClass.__subclasses__():
		if cls.Check(myStr):
			return cls()

# -- 2 --
def MyFactor2(myStr):
	for cls in BaseClass2.__subclasses__():
		if cls.Check(myStr):
			return cls()

print (MyFactor("ham").x)
print (MyFactor2("sandwich").x)
print (MyFactor2("pancakes").x)

# -- 3 --
class AltBaseClass(object):
	pass

class AltC1(AltBaseClass):
	def __init__(self, *args, **kwargs):
		self.x = 1
	def Check(self, myStr, *args, **kwargs):
		return myStr == "ham"

class AltC2(AltBaseClass):
	def __init__(self, *args, **kwargs):
		self.x = 30
	def Check(self, myStr, *args, **kwargs):
		return myStr == "sandwich"

def AltMyFactor(myStr):
	for cls in BaseClass.__subclasses__():
		if cls.Check(myStr):
			return cls()

print (AltMyFactor("ham").x)
print (AltMyFactor("sandwich").x)
print (AltMyFactor("pancakes").x)