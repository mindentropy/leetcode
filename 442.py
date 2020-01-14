#!/usr/bin/env python

class Solution(object):
	def findDuplicates(self, nums):
		
		op = []

		for idx in range(len(nums)):
			idx_c = abs(nums[idx])
			if nums[idx_c - 1] < 0:
				op.append(idx_c)
			else:
				nums[idx_c - 1] = -nums[idx_c - 1]

		return op

if __name__ == '__main__':
	nums = [4, 3, 2, 7, 8, 2, 3, 1]

	sol = Solution()
	print sol.findDuplicates(nums)
