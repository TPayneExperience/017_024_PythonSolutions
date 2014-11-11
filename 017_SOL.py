#!/usr/bin/env python

# -- 1 --
print (type("ham"))
print ("ham".__class__)

# -- 2 --
# don't remember why I asked this question
# ANSWER = Not unless you change the variable altogether
x = "ham"
try:
	x.__class__ = 'ham sandwich'
except:
	x = 1
print (x.__class__)


# -- 3 --
BaseClass = type("BaseClass", (object,), {'x':5})
SubClass = type("SubClass", (BaseClass,), {})

print (BaseClass.__subclasses__())

# -- 4 --
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            cls.x = 5
        return cls._instances[cls]
        
# class MyClass(object, metaclass = Singleton): ## PY 3.0+ USERS
class MyClass(object): ## PY 3.0+ USERS comment this out
    __metaclass__ = Singleton ## PY 3.0+ USERS comment this out
    def __init__(self, *args, **kwargs):
    	super(MyClass, self).__init__(*args, **kwargs)

m = MyClass()
v = MyClass()
print (type(m))
m.x = 9
print (v.x)
