#!/usr/bin/env python

class Solution(object):
	def restoreMatrix(self, rowSum, colSum):
		##TODO: Find the smallest in the colsum (Is this necessary?). From there select the 
		## first number and then subtract the row and col sums. Select the smallest of each row
		## and column
		
		matrix = [0] * len(rowSum)
		for idx in range(len(rowSum)):
			matrix[idx] = [0] * len(colSum)
		
		for row_idx in range(len(rowSum)):
			for col_idx in range(len(colSum)):
				min_val = min(rowSum[row_idx], colSum[col_idx])
				matrix[row_idx][col_idx] = min_val
				rowSum[row_idx] -= min_val
				colSum[col_idx] -= min_val

		return matrix

if __name__ == '__main__':
	#rowSum = [3, 8]
	#colSum = [4, 7]

	rowSum = [5, 7, 10]
	colSum = [8, 6, 8]

	sol = Solution()
	print(sol.restoreMatrix(rowSum,colSum))
