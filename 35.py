#!/usr/bin/env python

class Solution(object):
	def searchInsert(self, nums, target):
		low = 0
		high = len(nums) - 1

		while low <= high:
			mid = (low + high) >> 1
			
			if nums[mid] == target:
				return mid
			elif target > nums[mid]:
				low = mid + 1
			elif target < nums[mid]:
				high = mid - 1

		return high + 1

if __name__ == '__main__':
	sol = Solution()

	print('%d' % sol.searchInsert([1,2,3,6,7], 4))
