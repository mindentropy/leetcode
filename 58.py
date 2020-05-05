#!/usr/bin/env python

class Solution(object):
	def lengthOfLastWord(self, s):
		i = len(s) - 1

		lwlen = 0

		if s == '':
			return 0

		while(i >= 0 and s[i] == ' '):
			i -= 1

		while(i >= 0 and s[i] != ' '):
			i -= 1
			lwlen += 1

		return lwlen

if __name__ == '__main__':
	sol = Solution()
	print(sol.lengthOfLastWord('Hello World'))
