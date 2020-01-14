#!/usr/bin/env python

class Solution(object):
	def islandPerimeter(self, grid):
		rowidx = 0
		colidx = 0

		perimeter = 0

		for rowidx in range(len(grid)):
			for colidx in range(len(grid[0])):
				if grid[rowidx][colidx] == 1:
					perimeter += 4

					if rowidx > 0 and grid[rowidx - 1][colidx] == 1:
						perimeter -= 1

					if rowidx < (len(grid) - 1) and grid[rowidx + 1][colidx] == 1:
						perimeter -= 1

					if colidx > 0 and grid[rowidx][colidx - 1] == 1:
						perimeter -= 1


					if colidx < (len(grid[0]) - 1) and grid[rowidx][colidx + 1] == 1:
						perimeter -= 1

		return perimeter

if __name__ == '__main__':
	grid = [[0,1,0,0],
			[1,1,1,0],
			[0,1,0,0],
			[1,1,0,0]]

	sol = Solution()
	print sol.islandPerimeter(grid)
