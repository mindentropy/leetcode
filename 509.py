#!/usr/bin/env python

class Solution(object):
	def fib1(self, N):
		if N == 0:
			return 0
		elif N == 1:
			return 1

		num1 = 0
		num2 = 1
		for i in range(N-1):
			fib = num1 + num2
			num1 = num2
			num2 = fib

		return fib

	def fib(self, N):
		if N == 0:
			return 0
		elif N == 1:
			return 1
		
		return self.fib(N-1) + self.fib(N-2)

if __name__ == '__main__':
	sol = Solution()
	print sol.fib(4)

