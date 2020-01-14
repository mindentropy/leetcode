#!/usr/bin/env python

class Solution(object):
	def largestPerimeter(self, A):
		A.sort()

		for i in xrange(len(A) - 3, -1, -1):
			## c <= a + b
			## If c == a + b the triangle is degenerate
			if A[i] + A[i + 1] > A[i + 2]:
				return A[i+2] + A[i+1] + A[i]

		return 0

	def largestPerimeter(self, A):
		A.sort(reverse=True)

		for i in xrange(0, len(A) - 2, 1):
			## c <= a + b
			## If c == a + b the triangle is degenerate
			if A[i + 2] + A[i + 1] > A[i]:
				return A[i + 2] + A[i + 1] + A[i]

		return 0

if __name__ == '__main__':
	sol = Solution()

	print sol.largestPerimeter([1, 2, 1])
