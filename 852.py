#!/usr/bin/env python

class Solution(object):
	def peakIndexInMountainArray(self, A):
		idx = 1
		
		while A[idx] < A[idx + 1]:
			idx += 1

		return idx

		

if __name__ == '__main__':
	A = [0, 2, 1, 0]
	sol = Solution()
	print sol.peakIndexInMountainArray(A)
