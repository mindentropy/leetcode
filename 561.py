#!/usr/bin/env python

class Solution(object):
	def arrayPairSum(self, nums):
		nums.sort()

		idx = 0

		maxsum = 0

		nums_len = len(nums)

		while idx < nums_len:
			maxsum += nums[idx] if nums[idx] < nums[idx+1] else nums[idx+1]
			idx += 2

		return maxsum

if __name__ == '__main__':
	sol = Solution()
	print sol.arrayPairSum([1, 4, 3, 2])
