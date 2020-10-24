#!/usr/bin/env python

class Solution(object):
	
	def bin_search_neg(self, arr, lo, hi):
		if lo > hi:
			return -1
		else:
			mid = (lo + hi)//2

			if arr[mid] < 0:
				idx = mid

				while idx > 0 and arr[idx - 1] < 0:
					idx -= 1

				return idx
			elif arr[mid] >= 0:
				return self.bin_search_neg(arr, mid + 1, hi)
	
	def countNegatives(self, grid):
		totalneg = 0
		for arr in grid:
			idx = self.bin_search_neg(arr, 0, len(arr) - 1)
			if idx != -1:
				totalneg += len(arr) - idx

		return totalneg


if __name__ == '__main__':
	
	grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

	sol = Solution()
	print(sol.countNegatives(grid))
