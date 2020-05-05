#!/usr/bin/env python

class Solution(object):
	def judgeSquareSum(self, c):
		
		a = 0
		b = 0
		while(a*a <= c):
			b = a
			while(b * b <= c):
				if a*a + b*b == c:
					return True

				b += 1
			a += 1

		return False


if __name__ == '__main__':
	sol = Solution()

	print(sol.judgeSquareSum(999999999))
