#!/usr/bin/env python

class Solution(object):
	def climbStairs(self, n:int) -> int:

		if n == 1 or n == 2:
			return n
		else:
			prev = 1
			pres = 2
			i = 2
			while i < n:
				tmp = pres
				pres = pres + prev
				prev = tmp 

				i += 1
		
		return pres

if __name__ == '__main__':
	n = 5
	sol = Solution()
	print(sol.climbStairs(n))
