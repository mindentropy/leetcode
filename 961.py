#!/usr/bin/env python
from sets import Set

class Solution(object):
	def repeatedNTimes(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		s_idx = 0
		e_idx = len(A) - 1
		
		s = []

		while s_idx < e_idx:
			if A[s_idx] == A[e_idx]:
				return A[s_idx]
			elif A[s_idx] in s:
				return A[s_idx]
			elif A[e_idx] in s:
				return A[e_idx]
			else:
				s.append(A[s_idx])
				s.append(A[e_idx])

			s_idx += 1
			e_idx -= 1

		return A

if __name__ == '__main__':
	sol = Solution()

	A = [9, 5, 6, 9]

	print sol.repeatedNTimes(A)
