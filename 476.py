#!/usr/bin/env python

class Solution(object):
	def findComplement(self, num):
		bitstart = 1 << 31

		while (num & bitstart) == 0:
			bitstart >>= 1

		while bitstart:
			if num & bitstart == 0:
				num = num|bitstart
			else:
				num &= ~bitstart

			bitstart >>= 1

		return num

if __name__ == '__main__':
	sol = Solution()

	print sol.findComplement(5)
