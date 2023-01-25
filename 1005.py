#!/usr/bin/env python

class Solution(object):
	def largestSumAfterKNegations(self, nums, k):
		nums.sort()

		idx = 0

		while k > 0:
			nums[idx] = -nums[idx]

			if idx < len(nums) - 1 and nums[idx] > nums[idx + 1]:
				idx = idx + 1

			k = k - 1
		
		return sum(nums)

if __name__ == '__main__':
	nums = [-4, -2, -3]
	k = 4

	sol = Solution()
	
	print(sol.largestSumAfterKNegations(nums, k))
