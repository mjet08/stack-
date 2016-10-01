#!usr/bin/python

class stackk(object):
	
	def __init__(self,limit):
		self.stk=[]
		self.limit = limit
		
	
	def push(self,item):
		if (len(self.stk)>=self.limit):
			print("stack overflow")
			
		else:
			self.stk.append(item)
			
			
	def pop(self):
		if(len(self.stk)<=0):
			print("stack underflow")
		
		else:
			return self.stk.pop()
			
			
	def isEmpty(self):
		return len(self.stk)==0
		
	def peek(self):
		if (len(self.stk)<=0):
			print("stack underflow")
			
		else:
			return self.stk[-1]
			
			
	
stk = stackk(5)
stk.push("hi")

print(stk.pop())