#!/usr/bin/env python

from typing import List

#class Solution(object):
#	def countBits(self, num: int) -> List[int]:
#		ans = [0] * (num + 1)
#		
#		b = 1
#		i = 0
#		while b <= num:
#			while i < b and (i + b) <= num:
#				## ans[i] will be the previous blocks.
#				## ans[i + b] will be the present blocks.
#				ans[i + b] = ans[i] + 1
#				i += 1
#
#			i = 0
#			b <<= 1
#			
#		return ans

class Solution(object):
	def countBits(self, num: int) -> List[int]:
		ans = [0] * (num + 1)

		for i in range(1, num):
			ans[i] = ans[ i>>1 ] + (i & 1)

		return ans

if __name__ == '__main__':
	n = 2
	sol = Solution()
	print(sol.countBits(n))
