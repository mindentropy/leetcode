#!/usr/bin/env python

class MinStack:

	def __init__(self):
		self.stk = []
		self.min = 0

	def push(self, x: int) -> None:
		if self.stk == []:
			self.min = x
		else:
			if self.min > x:
				self.min = x

		self.stk.append(x)

	def pop(self) -> None:
		if self.stk == []:
			return

		val = self.stk.pop()

		if self.min == val:
			##O(n) here????
			if self.stk != []:
				self.min = min(self.stk)

	def top(self) -> int:
		return self.stk[-1]
	
	def getMin(self) -> int:
		return self.min

if __name__ == '__main__':
	minstk = MinStack()

	minstk.push(-2)
	minstk.push(0)
	minstk.push(-3)

	print(minstk.getMin())
	minstk.pop()

	print(minstk.top())
	print(minstk.getMin())
