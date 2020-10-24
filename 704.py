#!/usr/bin/env python

class Solution(object):
	def bin_search(self, nums, low, high, target):
		if low > high:
			return -1
		else:
			mid = (low + high)//2

			if target == nums[mid]:
				return mid
			elif target > nums[mid]:
				return self.bin_search(nums, mid + 1, high, target)
			else:
				return self.bin_search(nums, low, mid - 1, target)

	def search(self, nums, target):
		return self.bin_search(nums, 0, len(nums) - 1, target)

if __name__ == '__main__':
	sol = Solution()
	nums = [-1, 0, 3, 5, 9, 12]
	target = 2

	print(sol.search(nums, target))
