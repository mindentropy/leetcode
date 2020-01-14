#!/usr/bin/env python

class Solution(object):
	def transpose(self, A):
		B = []
		row = len(A)
		col = len(A[0])

		for row_idx in range(col):
			col = []
			for col_idx in range(row):
				col.append(A[col_idx][row_idx])
			B.append(col)

		return B

if __name__ == '__main__':

	A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	sol = Solution()

	print sol.transpose(A)
