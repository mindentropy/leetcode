#!/usr/bin/env python

class Solution(object):
	def isAnagram(self, s, t):
		if len(s) != len(t):
			return False
		
		alpha_cnt = [0] * 26

		for idx in xrange(len(s)):
			alpha_cnt[ord(s[idx]) - 97] += 1
			alpha_cnt[ord(t[idx]) - 97] -= 1
			
		
		for idx in xrange(26):
			if alpha_cnt[idx] != 0:
				return False

		return True
		
if __name__ == '__main__':
	sol = Solution()

	print sol.isAnagram('car', 'rac')
