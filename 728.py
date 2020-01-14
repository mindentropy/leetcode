#!/usr/bin/env python

class Solution(object):

	def selfDividingNumbers(self, left, right):
		op = []

		while left <= right:
			num = left
			
			while num != 0:
				val = num % 10

				if val == 0 or left % val != 0:
					break

				num = num / 10
			
			if num == 0:
				op.append(left)

			left += 1

		return op

if __name__ == '__main__':

	sol = Solution()
	left = 1
	right = 22
	print sol.selfDividingNumbers(left, right)
