#!/usr/bin/env python

class Solution(object):
	def findDisappearedNumbers(self, nums):

		for idx in xrange(len(nums)):
			idx_c = abs(nums[idx]) - 1
			nums[idx_c] = -nums[idx_c]

		print nums

if __name__ == '__main__':
	nums = [2, 1, 2 ,4]
	sol = Solution()
	sol.findDisappearedNumbers(nums)
