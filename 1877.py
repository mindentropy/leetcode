#!/usr/bin/env python

class Solution(object):
	def minPairSum(self, nums):
		nums.sort()
		
		start = 0
		end = len(nums) - 1

		max_val = 0

		while start < end:
			total = nums[start] + nums[end]
			if max_val < total:
				max_val = total

			start += 1
			end -= 1


		return max_val

if __name__ == '__main__':
	nums = [3, 5, 2, 3]

	sol = Solution()
	print(sol.minPairSum(nums))
