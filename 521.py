#!/usr/bin/env python

class Solution(object):
	def findLUSlength(self, a, b):
		
		if a == b:
			return -1
		elif len(a) == len(b):
			return len(a)
		else:
			return max(len(a), len(b))

if __name__ == '__main__':
	sol = Solution()
	print sol.findLUSlength('aba', 'cdc')
