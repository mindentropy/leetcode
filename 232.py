#!/usr/bin/env python

class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.stk1 = list()
		self.stk2 = list()

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""

		while len(self.stk2):
			self.stk1.append(self.stk2.pop())

		self.stk1.append(x)

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""

		while len(self.stk1):
			self.stk2.append(self.stk1.pop())
		
		return self.stk2.pop()

	def peek(self) -> int:
		"""
		Get the front element.
		"""

		while len(self.stk1):
			self.stk2.append(self.stk1.pop())

		return self.stk2[-1]

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""

		if len(self.stk1) == 0 and len(self.stk2) == 0:
			return True
		else:
			return False
 
if __name__ == '__main__':
	queue = MyQueue()
	queue.push(1)
	queue.push(2)

	print(queue.peek())
	print(queue.pop())

	print(queue.empty())
