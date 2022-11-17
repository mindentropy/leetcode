#!/usr/bin/env python

class Solution(object):
	def isSubsequence(self, s: str, t: str) -> bool:

		src_idx = 0
		dest_idx = 0
		
		while src_idx < len(s) and dest_idx < len(t):
			if s[src_idx] == t[dest_idx]:
				src_idx += 1

			dest_idx += 1

		if src_idx < len(s) and dest_idx == len(t):
			return False

		return True

if __name__ == '__main__':
	s = 'aaaaaa'
	t = 'bbaaaa'
	
#	s = 'abc'
#	t = 'ahbgdc'

	sol = Solution()
	print(sol.isSubsequence(s, t))
