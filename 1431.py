#!/usr/bin/env python

from typing import List

class Solution(object):
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		op = []
		total = []
		
		maxcandy = 0
		for val in candies:

			if val > maxcandy:
				maxcandy = val

			total += [val + extraCandies]

		for val in total:
			if val < maxcandy:
				op += [False]
			else:
				op += [True]

		return op
			

if __name__ == '__main__':

	candies = [2, 3, 5, 1, 3]
	extraCandies = 3

	sol = Solution()
	print(sol.kidsWithCandies(candies, extraCandies))
