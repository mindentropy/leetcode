#!/usr/bin/env python

#class Solution(object):
#	def tribonacci(self, n):
#		if n == 0:
#			return 0
#		elif n == 1:
#			return 1
#		elif n == 2:
#			return 1
#		else:
#			return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

class Solution(object):
	def trib_memoization(self, n, a):
		if n == 0:
			return 0
		elif n == 1 or n== 2:
			return 1
		else:
			a[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

			return a[n]

	def tribonacci(self, n):
		return self.trib_memoization(n, [0] * (n+1))


class Solution(object):
	def tribonacci(self, n):
		if n == 0:
			return 0
		elif n == 1 or n == 2:
			return 1

		trib = 0
		tmp = 0
		num1 = 0
		num2 = 1
		num3 = 1

		for i in range(n - 2):
			tmp = trib
			trib = num1 + num2 + num3
			num1 = num2
			num2 = num3
			num3 = trib

		return trib

if __name__ == '__main__':
	
	sol = Solution()
	print sol.tribonacci(3)
