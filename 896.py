#!/usr/bin/env python

class Solution(object):
	def isMonotonic(self, A):
		if len(A) == 1:
			return True
		
		i = 1
		while (i < len(A)) and A[i] == A[0]:
			i += 1

		prev = A[i-1]

		incr = True
		if A[i-1] == A[0] and i == len(A):
			return True

		if A[i] < A[0]:
			incr = False

		for idx in xrange(i, len(A)):
			if incr:
				if A[idx] < prev:
					return False
			else:
				if A[idx] > prev:
					return False

			prev = A[idx]

		return True

if __name__ == '__main__':
	sol = Solution()
	print sol.isMonotonic([1, 1 ,1])
