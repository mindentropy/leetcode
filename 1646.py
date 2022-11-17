#!/usr/bin/env python

class Solution(object):
	def getMaximumGenerated(self, n:int) -> int:
		nums = [0] * (n + 1)

		if n == 0 or n == 1:
			return n

		nums[0] = 0
		nums[1] = 1

		max_val = -1
		for i in range(2, n + 1):
			nums[i] = nums[i>>1] + (i & 1) * nums[(i>>1) + 1]

			if nums[i] > max_val:
				max_val = nums[i]

		return max_val

if __name__ == '__main__':
	n = 7
	sol = Solution()
	print(sol.getMaximumGenerated(n))
