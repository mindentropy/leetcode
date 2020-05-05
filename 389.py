#!/usr/bin/env python

class Solution1(object):
	def findTheDifference(self, s, t):
		s = sorted(s)
		t = sorted(t)

		idx = 0
		for idx in xrange(len(s)):
			if s[idx] != t[idx]:
				return t[idx]

		return t[-1]

class Solution(object):
	def findTheDifference(self, s, t):
		cnt = 0

		for idx in xrange(len(s)):
			cnt += ord(s[idx])

		for idx in xrange(len(t)):
			cnt -= ord(t[idx])

		return chr(abs(cnt))

if __name__ == '__main__':
	sol = Solution()
	print sol.findTheDifference('abcd', 'abcde')
