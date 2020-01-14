#!/usr/bin/env python

class Solution(object):
	def sortedSquares(self, A):

		right_idx = 0

		for val in A:
			if A[right_idx] < 0:
				right_idx += 1

		left_idx = right_idx - 1
			

		op = []
		while True:
			
			if left_idx < 0 and right_idx >= len(A):
				break

			if left_idx < 0 and right_idx < len(A):
				op.append(A[right_idx] * A[right_idx])
				right_idx += 1
				continue
			elif left_idx >= 0 and right_idx >= len(A):
				op.append(A[left_idx] * A[left_idx])
				left_idx -= 1
				continue
			
			if A[right_idx] >= -A[left_idx]:
				op.append(A[left_idx] * A[left_idx])
				left_idx -= 1
			elif A[right_idx] < -A[left_idx]:
				op.append(A[right_idx] * A[right_idx])
				right_idx += 1

		return op

if __name__ == '__main__':

	a = [-7,-3,2,3,11]

	sol = Solution()
	print sol.sortedSquares(a)
