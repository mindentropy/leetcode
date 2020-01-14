#!/usr/bin/env python

class Solution(object):
	def flipAndInvertImage(self, A):
		"""
		:type A: List[List[int]]
		:rtype: List[List[int]]
		"""
		rows = len(A)
		cols = len(A[0])
		
		start_col_idx = 0
		end_col_idx = cols - 1

		while start_col_idx <= end_col_idx:
			for row_idx in range(rows):
				if A[row_idx][start_col_idx] == A[row_idx][end_col_idx]:
					if A[row_idx][start_col_idx] == 1:
						A[row_idx][start_col_idx] = 0
					else:
						A[row_idx][start_col_idx] = 1
					
					if start_col_idx != end_col_idx: 
						if A[row_idx][end_col_idx] == 1:
							A[row_idx][end_col_idx] = 0
						else:
							A[row_idx][end_col_idx] = 1
			
			start_col_idx += 1
			end_col_idx -= 1

		return A

if __name__ == '__main__':
	sol = Solution()
	
	A = [	
			[1, 1, 0],
			[1, 0, 1],
			[0, 0, 0]
		]

#	A = [	
#			[1, 1, 0, 0],
#			[1, 0, 0, 1],
#			[0, 1, 1, 1],
#			[1, 0, 1, 0]
#		]

	print(sol.flipAndInvertImage(A))
