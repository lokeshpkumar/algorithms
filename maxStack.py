#!/usr/bin/python

class MaxStack:
    def __init__(self):
        self.arr = list()
        self.maxs = list()
        print "Initialized the stack"
  
    def push(self, val):
        self.arr.append(val)
        if self.maxs:
            self.maxs.append(max(val, self.maxs[-1]))
        else:
            self.maxs.append(val)
  
    def pop(self):
        if self.maxs:
            self.maxs.pop()
        return self.arr.pop()
  
    def max(self):
        return self.maxs[-1]
    
    def __str__(self):
        return "{0}".format(self.arr)
  
s = MaxStack()
s.push(1)
print str(s)
s.push(2)
print str(s)
s.push(3)
print str(s)
s.push(2)
print str(s)
print s.max()

s.pop()
print str(s)
s.pop()
print str(s)
print s.max()
