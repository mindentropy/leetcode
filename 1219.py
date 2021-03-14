#!/usr/bin/env python

from typing import List

class Solution(object):
	def __init__(self):
		self.max_val = 0

	def getMaxGold(self, grid: List[List[int]], incr, row, col, lst, trav_lst):
		for k in range(len(incr)):
			new_row = row + incr[k][0]
			new_col = col + incr[k][1]
			
			if new_row >= 0 and new_row < len(grid) and  \
				new_col >=0 and new_col < len(grid[0]) and \
				grid[new_row][new_col] != 0 and not (new_row, new_col) in trav_lst:

				tmpval = grid[new_row][new_col]
				self.getMaxGold(grid,
								incr,
								new_row,
								new_col,
								lst + [tmpval],
								trav_lst + [(new_row, new_col)])
			else:
				if sum(lst) > self.max_val:
					self.max_val = sum(lst)
		
	def getMaximumGold(self, grid: List[List[int]]) -> int:
		incr = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
		for ridx in range(len(grid)):
			for cidx in range(len(grid[ridx])):
				if grid[ridx][cidx] != 0:
					lst = []
					trav_lst = []
					self.getMaxGold(grid, incr, ridx, cidx,
							lst + [grid[ridx][cidx]], trav_lst + [(ridx, cidx)] )

		return(self.max_val)


if __name__ == '__main__':
	
	grid = [
			[0, 6, 0],
			[5, 8, 7],
			[0, 9, 0]]

	sol = Solution()
	sol.getMaximumGold(grid)

	#incr = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
	#k = 0
	#while k < 4:
	#	print(incr[k][0])
	#	k += 1
