#!/usr/bin/env python

class Solution(object):
	def minCostToMoveChips(self, chips):
		odd = even = 0

		for val in chips:
			if (val & 1) == 0:
				even += 1
			else:
				odd += 1

		return min(even, odd)

if __name__ == '__main__':

	chips = [2, 2, 2, 3, 3]

	sol = Solution()
	print sol.minCostToMoveChips(chips)
