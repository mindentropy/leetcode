#!/usr/bin/env python

class Solution(object):
	def bitwiseComplement(self, N):
		op = 0
		idx = 0

		if N == 0:
			return 1

		while(N):
			if not (N & 1):
				op |= 1<<idx
			N >>= 1
			idx += 1

		return op

if __name__ == '__main__':
	sol = Solution()
	print sol.bitwiseComplement(5)
