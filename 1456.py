#!/usr/bin/env python

class Solution(object):
	def maxVowels(self, s, k):
		slen = len(s) - k + 1
		vowelstr = 'aeiou'
		idx1 = 0
		maxcnt = 0
	
		vowcnt = 0
		while idx1 < k:
			if s[idx1] in vowelstr:
				vowcnt += 1
			idx1 += 1

		maxcnt = vowcnt

		idx1 = 1
		while idx1 < slen:

			if s[idx1 - 1] in vowelstr:
				vowcnt -= 1

			if s[idx1 + k - 1] in vowelstr:
				vowcnt += 1

			if vowcnt > maxcnt:
				maxcnt = vowcnt
				
				if maxcnt == k:
					break

			idx1 += 1

		return maxcnt

if __name__ == '__main__':
	s = 'weallloveyou'
	k = 7

	sol = Solution()
	print(sol.maxVowels(s, k))
