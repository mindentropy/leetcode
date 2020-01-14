#!/usr/bin/env python

class Solution(object):
	def shift(self, grid):
		rowsize = len(grid)
		colsize = len(grid[0])

		tmpcol = [0] * rowsize

		for idx in xrange(rowsize):
			tmpcol[idx] = grid[idx][colsize - 1]
		
		for idx in xrange(rowsize):
			grid[idx] = grid[idx][:-1]

		for idx in xrange(1, rowsize):
			grid[idx] = [tmpcol[idx - 1]] + grid[idx]

		grid[0] = [tmpcol[-1]] + grid[0]
	
		return grid

	def shiftGrid(self, grid, k):
		while k > 0:
			grid = self.shift(grid)
			k -= 1

		return grid
		
if __name__ == '__main__':
	grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
	sol = Solution()
	print sol.shiftGrid(grid, 4)
