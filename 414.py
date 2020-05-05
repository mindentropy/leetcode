#!/usr/bin/env python

class Solution(object):
	def thirdMax(self, nums):
		max_nums = [-2147483649] * 3

		for idx in xrange(len(nums)):
			if nums[idx] > max_nums[0]:
				max_nums[2] = max_nums[1]
				max_nums[1] = max_nums[0]
				max_nums[0] = nums[idx]
			elif nums[idx] > max_nums[1] and nums[idx] != max_nums[0]:
				max_nums[2] = max_nums[1]
				max_nums[1] = nums[idx]
			elif nums[idx] > max_nums[2] and nums[idx] != max_nums[1] and nums[idx] != max_nums[0]:
				max_nums[2] = nums[idx]

		print max_nums
		if max_nums[2] != -2147483649:
			return max_nums[2]
		else:
			return max_nums[0]

if __name__ == '__main__':
	sol = Solution()
	print sol.thirdMax([1, 2, 2, 5, 3, 5])
