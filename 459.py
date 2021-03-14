#!/usr/bin/env python

class Solution(object):
	def repeatedSubstringPattern(self, s: str) -> bool:

		slen = len(s)

		if slen == 1:
			return False

		if slen == 2:
			return s[0] == s[1]

		mid = 1
		while mid <= slen//2:
			midx = mid
			while midx < slen:
				if s[0:mid] == s[midx:midx+len(s[0:mid])]:
					if (midx + len(s[0:mid])) > slen:
						return True
					else:
						midx += len(s[0:mid])
				else:
					mid += 1
					break

			if midx >= slen:
				return True

		if mid >= slen//2:
			return False

if __name__ == '__main__':
	s = 'zzz'
	sol = Solution()
	print(sol.repeatedSubstringPattern(s))
