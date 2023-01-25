#!/usr/bin/env python

class Solution(object):
	def maxIncreaseKeepingSkyline(self, grid):
		horiz_max = [0] * len(grid[0])
		vert_max = [0] * len(grid[0])

		for idx in range(len(grid[0])):
			vert_max[idx] = max(grid[idx])
			for idx1 in range(len(grid[0])):
				if horiz_max[idx1] < grid[idx][idx1]:
					horiz_max[idx1] = grid[idx][idx1]

		total = 0
		for row in range(len(grid[0])):
			for col in range(len(grid[0])):
				total += min(horiz_max[col], vert_max[row]) - grid[row][col]

		return total

if __name__ == '__main__':
	
	grid = [[3, 0, 8, 4],
			[2, 4, 5, 7],
			[9, 2, 6 ,3],
			[0, 3, 1, 0]]

	sol = Solution()
	print(sol.maxIncreaseKeepingSkyline(grid))
