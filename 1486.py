#!/usr/bin/env python

class Solution:
	def xorOperation(self, n:int, start:int) -> int:

		if n == 1:
			return start

		xornum = start ^ (start + (2 * (n - 1)))
		
		idx = 1
		end = n - 2
		while idx < end:
			xornum ^= (start + 2 * idx) ^ (start + 2 * end);
			
			idx += 1
			end -= 1
			
		if n & 1:
			xornum ^= start + 2 * idx

		return xornum

if __name__ == '__main__':

	n = 4
	start = 3

	sol = Solution()

	print(sol.xorOperation(n, start))
