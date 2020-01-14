#!/usr/bin/env python

class Solution(object):
	def maxNumberOfBalloons(self, text):
		freq = dict()

		for idx in xrange(len(text)):
			freq[text[idx]] = freq.get(text[idx], -1) + 1

		maxcnt = 0
		while True:
			for val in 'balloon':

				if val not in freq:
					return maxcnt

				if freq[val] == -1:
					return maxcnt

				freq[val] -= 1

			maxcnt += 1

if __name__ == '__main__':
	text = 'balon'
	sol = Solution()
	print sol.maxNumberOfBalloons(text)
