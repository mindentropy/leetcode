#!/usr/bin/env python

class Solution(object):
	def validPalindrome(self, s):
		start = 0
		end = len(s) - 1
		log = 0
		
		if len(s) in [1, 2]:
			return True
		elif len(s) == 3:
			if s[start] != s[end] and (s[start + 1] != s[end] or s[end - 1] != s[start]):
				return False
			else:
				return True

		while start < end:
			if s[start] == s[end]:
				start += 1
				end -= 1
			else:
				if log == 1:
					return False

				if s[start + 1] == s[end]:
					start += 1
					log += 1
				elif s[start] == s[end - 1]:
					end -= 1
					log += 1
				else:
					return False

		if start == end or start > end:
			return True

if __name__ == '__main__':
	sol = Solution()
	s = 'abbab'
	print(sol.validPalindrome(s))
