#!/usr/bin/env python

## Solution is TLE (Time Limit Exceeded)
## Solution needs to be optimized based on basic understanding

class Solution(object):
	def findUnsortedSubarray(self, nums):
		left = len(nums) - 1
		right = 0

		if len(nums) == 0 or len(nums) == 1:
			return 0

		for i in xrange(len(nums)):
			for j in xrange(i + 1, len(nums)):
				if nums[j]  < nums[i]:
					left = min(left, i)
					right = max(j, right)
						
		if (right - left) < 0:
			return 0
		else:
			return right - left + 1

if __name__ == '__main__':
	sol = Solution()
	print sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
