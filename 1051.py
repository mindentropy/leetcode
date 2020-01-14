#!/usr/bin/env python

class Solution(object):
	def heightChecker(self, heights):
		height_sort = sorted(heights)

		count = 0
		for idx in range(len(heights)):
			if heights[idx] != height_sort[idx]:
				count = count + 1

		return count

if __name__ == '__main__':

	heights = [1, 1, 4, 2, 1, 3]
	sol = Solution()
	print sol.heightChecker(heights)
