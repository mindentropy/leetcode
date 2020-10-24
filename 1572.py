#!/usr/bin/env python

class Solution(object):
	def diagonalSum(self, mat):
		sl = len(mat[0])
		
		if sl == 1:
			return mat[0][0]

		diagsum = 0
		idx = 0

		for idx in range(sl):
			diagsum += mat[idx][idx]
			diagsum += mat[sl - idx - 1][idx]

		if sl & 1:
			diagsum -= mat[sl>>1][sl>>1]

		return diagsum

if __name__ == '__main__':
	sol = Solution()
	mat = [[1, 2, 3],
		 	[4, 5, 6],
			[7, 8, 9]]

	mat = [[1, 1, 1, 1],
			[1, 1, 1, 1],
			[1, 1, 1, 1],
			[1, 1, 1, 1]]

	mat = [[7, 3, 1, 9],
			[3, 4, 6, 9],
			[6, 9, 6, 6],
			[9, 5, 8, 5]]

	print(sol.diagonalSum(mat))
