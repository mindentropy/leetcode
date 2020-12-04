#!/usr/bin/env python

class Solution(object):
	def longestOnes(self, A, K):
		idx1 = idx2 = 0
		maxcnt = 0
		kcnt = 0
	
		while idx2 < len(A):
			

if __name__ == '__main__':
	#	[1, 1, 1, 0, 1, 0, 0, 0]
	#A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
	#K = 2
	#A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
	#K = 3
	A = [0, 0, 0, 1]
	K = 4

	sol = Solution()
	print(sol.longestOnes(A, K))
