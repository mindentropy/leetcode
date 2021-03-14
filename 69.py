#!/usr/bin/env python

class Solution(object):
	def mySqrt(self, x):
		lo = 1
		hi = x + 1

		while(lo <= hi):
			mid = (lo + hi) / 2
			
			if mid * mid == x:
				return mid
			if mid * mid <= x:
				lo = mid + 1
			else:
				hi = mid - 1

		return lo

if __name__ == '__main__':
	sol = Solution()
	print(sol.mySqrt(4))
