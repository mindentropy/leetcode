#!/usr/bin/env python

class Solution(object):
	def titleToNumber(self, s):

		idx = len(s) - 1
		op = 0

		multiplier = 1
		while idx >= 0:
			op += (ord(s[idx]) - (ord('A') - 1)) * multiplier
			multiplier *= 26
			idx -= 1

		return op

if __name__ == '__main__':
	sol = Solution()
	print sol.titleToNumber('ZY')
