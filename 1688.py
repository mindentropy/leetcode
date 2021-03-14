#!/usr/bin/env python

class Solution(object):
	def numberOfMatches(self, n: int) -> int:
		if n == 1:
			return 0

		if n & 1: ## Odd
			return self.numberOfMatches(int((n/2)) + 1) + int(n/2)
		else:
			return self.numberOfMatches(int(n/2)) + int(n/2)
		
if __name__ == '__main__':
	sol = Solution()
	print(sol.numberOfMatches(7))
	
