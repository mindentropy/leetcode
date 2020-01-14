#!/usr/bin/env python

class Solution1(object):
	def fairCandySwap(self, A, B):
		asum = 0
		bsum = 0
		op = []
		for val in A:
			asum += val

		for val in B:
			bsum += val
		
		for idx1 in xrange(len(A) - 1, -1, -1):
			for idx2 in xrange(len(B)):
				if A[idx1] == B[idx2]:
					continue
				elif (asum - A[idx1] + B[idx2]) == (bsum - B[idx2] + A[idx1]):
					return [A[idx1], B[idx2]]

class Solution(object):
	def fairCandySwap(self, A, B):
		asum = 0
		bsum = 0
		
		asum = sum(A)
		bsum = sum(B)
		
		bset = set(B)

		for x in A:
			if (((bsum - asum)//2) + x) in bset:
				return [x, ((bsum - asum)//2) + x]
				

if __name__ == '__main__':
	A = [1, 2]
	B = [2, 3]

	sol = Solution()
	print sol.fairCandySwap(A, B)
