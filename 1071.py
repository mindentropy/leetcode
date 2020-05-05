#!/usr/bin/env python

class Solution(object):
	def gcdOfStrings(self, str1, str2):
		siz1 = len(str1)
		siz2 = len(str2)

		siz = min(siz1, siz2)



if __name__ == '__main__':
	sol = Solution()
	sol.gcdOfStrings('ABCABC', 'ABC')
