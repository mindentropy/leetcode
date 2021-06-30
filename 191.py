#!/usr/bin/env python

class Solution(object):
#	def hammingWeight(self, n):
#		bitcnt = 0
#		while(n):
#			if n & 1:
#				bitcnt += 1
#			n >>= 1
#
#		return bitcnt

	def hammingWeight(self, n: int) -> int:
		bitcnt = 0

		while(n):
			n = n & (n - 1)
			bitcnt += 1

		return bitcnt

if __name__ == '__main__':
	sol = Solution()
	n = 255
	print(sol.hammingWeight(n))
