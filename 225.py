#!/usr/bin/env python

from queue import SimpleQueue

class MyStack:
	def __init__(self):
		self.que = SimpleQueue()

	def push(self, x: int) -> None:
		self.que.put(x)

	def pop(self) -> int:
		qlen = self.que.qsize()
		qlen -= 1
		while qlen > 0:
			self.que.put(self.que.get())
			qlen -= 1

		return self.que.get()

	def top(self) -> int:
		qlen = self.que.qsize()
		
		qlen -= 1

		while qlen > 0:
			self.que.put(self.que.get())
			qlen -= 1

		val = self.que.get()
		self.que.put(val)

		return val

	def empty(self) -> bool:
		return self.que.empty()

if __name__ == '__main__':

	obj = MyStack()
	obj.push(1)
	obj.push(2)

	print(obj.top())
	print(obj.pop())

	print(obj.empty())
