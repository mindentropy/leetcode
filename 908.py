#!/usr/bin/env python

class Solution(object):
	def smallestRangeI(self, A, K):
		minval = 10000
		maxval = 0

		for val in A:
			if val < minval:
				minval = val
			if val > maxval:
				maxval = val
		
		if minval == maxval:
			return maxval - minval

		minidx = maxidx = 0
		while maxval >= minval:
			if minidx < K:
				minval += 1
				minidx += 1

			if maxidx < K:
				maxval -= 1
				maxidx += 1

			if maxidx == K or minidx == K:
				break

		if maxval - minval < 0:
			return 0
		else:
			return maxval - minval

if __name__ == '__main__':

	A = [7, 7, 7]
	K = 4

	sol = Solution()
	print sol.smallestRangeI(A, K)
