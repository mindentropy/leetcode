#!/usr/bin/env python

class CustomStack(object):
	
	def __init__(self, maxSize: int):
		self.stk = [0] * maxSize
		self.top = -1
	
	def push(self, x: int) -> None:
		if self.top != len(self.stk) - 1:
			self.top += 1
			self.stk[self.top] = x

	def pop(self) -> int:
		if self.top != -1:
			val = self.stk[self.top]
			self.top = self.top - 1
			return val
		else:
			return -1

	def increment(self, k:int ,val: int) -> None:
		if k > self.top:
			k = self.top
		else:
			k -= 1
		
		while k >= 0:
			self.stk[k] += val
			k -= 1

if __name__ == '__main__':
	obj = CustomStack(3)

	obj.push(1)
	obj.push(2)
	obj.push(3)
	obj.push(4)
	
	obj.increment(5, 100)
	obj.increment(2, 100)

	print(obj.stk)
	print(obj.top)
