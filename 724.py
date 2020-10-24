#!/usr/bin/env python3

from typing import List

class Solution:
	def pivotIndex(self, nums: List[int]) -> int:
		arr_len = len(nums)

		if arr_len == 0:
			return -1

		pi = 0
		leftsum = 0
		rightsum = 0
		while pi+1 < arr_len:
			rightsum += nums[pi + 1]
			pi += 1
		
		if leftsum == rightsum:
			return 0
	
		pi = 1
		while pi < arr_len:
			leftsum += nums[pi - 1]
			rightsum -= nums[pi]

			if leftsum == rightsum:
				return pi

			pi += 1

		return -1

if __name__ == '__main__':
	sol = Solution()
	nums = [-1, -1, -1, 0, 1, 1]

	print(sol.pivotIndex(nums))
