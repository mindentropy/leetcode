#!/usr/bin/env python

class Solution(object):
	def numSpecialEquivGroups(self, A):
		s = set()

		for string in A:
			odd_even = [0] * 52
			for idx in range(len(string)):
				odd_even[ord(string[idx]) - ord('a') + 26 * (idx & 1)] += 1
			s.add(tuple(odd_even))

		return len(s)

if __name__ == '__main__':
	A = ['abcd', 'cdab', 'cbad', 'xyzz', 'zzxy', 'zzyx']
	
	sol = Solution()
	print sol.numSpecialEquivGroups(A)
