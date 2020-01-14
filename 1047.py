#!/usr/bin/env python

class Solution(object):
	def removeDuplicates(self, S):
		strlst = list(S)

		resultlst = []

		for ch in strlst:
			if len(resultlst) != 0 and resultlst[-1] == ch:
				resultlst.pop()
			else:
				resultlst.append(ch)

		return ''.join(resultlst)

if __name__ == '__main__':
	s = 'abbaca'
	sol = Solution()
	print sol.removeDuplicates(s)
