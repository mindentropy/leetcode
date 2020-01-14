#!/usr/bin/env python

class Solution(object):

	def reverseWords(self, s):
		
		strlen = len(s)

		if strlen == 0:
			return s

		s = list(s)
		startidx = 0

		for idx in range(strlen):
			if s[idx] == ' ':
				endidx = idx - 1
				
				while(startidx < endidx):
					s[startidx], s[endidx] = s[endidx], s[startidx]
					startidx += 1
					endidx -= 1

				startidx = idx + 1

		endidx = idx
		
		while(startidx < endidx):
			s[startidx], s[endidx] = s[endidx], s[startidx]
			startidx += 1
			endidx -= 1

		return ''.join(s)

if __name__ == '__main__':
	sol = Solution()
	string = "Let's take LeetCode contest"
	print sol.reverseWords(string)
