#!/usr/bin/env python


class Solution(object):
	def hasAlternatingBits(self, n):
		while(n):
			if not ((n & 1) ^ ((n>>1) & 1)):
				return False

			n >>= 1

		return True

if __name__ == '__main__':
	
	sol = Solution()
	print sol.hasAlternatingBits(10)
