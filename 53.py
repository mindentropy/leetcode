#!/usr/bin/env python

class Solution(object):
	def maxSubArray(self, nums):

		if len(nums) == 0:
			return nums[0]

		cur_max_sum = nums[0]
		running_sum = nums[0]

		for idx in range(1, len(nums)):
			if running_sum < 0 and nums[idx] < 0:
				if cur_max_sum < nums[idx]:
					cur_max_sum = nums[idx]
				running_sum = nums[idx] ## Reset the running sum, because adding
										## two neg numbers won't give max sum
			elif running_sum >= 0 and nums[idx] >= 0:
				running_sum += nums[idx] ## Two positive number additions will 
										## give a higher max sum
			elif running_sum < 0 and nums[idx] >= 0: ## Adding a neg to a positive
				running_sum = nums[idx] ## won't give a higher max sum. Hence reset
			elif running_sum >= 0 and nums[idx] < 0:
				if cur_max_sum < running_sum: ## We are going to go neg
					cur_max_sum = running_sum ## Hence check the value and save
				running_sum += nums[idx]

		if cur_max_sum < running_sum:
			cur_max_sum = running_sum

		return cur_max_sum

if __name__ == '__main__':
	sol = Solution()
	nums = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
	print(sol.maxSubArray(nums))
