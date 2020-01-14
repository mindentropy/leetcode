#!/usr/bin/env python

class Foo(object):
	def __init__(self):
		self.f = False
		self.s = False

	def first(self, printFirst):
		self.f = True
		printFirst()
	
	def second(self, printSecond):
		if self.f == False:
			return
		
		self.second = True
		printSecond()

	def third(self, printThird):
		if self.s == False:
			return

		printThird()


if __name__ == '__main__':
	
