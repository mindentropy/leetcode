#!/usr/bin/env python

class Solution(object):
	def detectCapitalUse(self, word):
		if len(word) == 1:
			return True

		if word[0].isupper() and word[1].isupper():
			if len(word) > 2:
				for idx in xrange(2, len(word)):
					if not word[idx].isupper():
						return False

				return True
			else:
				return True
		else:
			for idx in xrange(1, len(word)):
				if word[idx].isupper():
					return False

			return True

if __name__ == '__main__':
	sol = Solution()
	print sol.detectCapitalUse('leetCode')
