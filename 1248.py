#!/usr/bin/env python

from typing import List

class Solution(object):
	def numberOfSubarrays(self, nums: List[int], k: int) -> int:
		next_odd = []

		for idx in range(len(nums)):
			if nums[idx] & 1 == 1:
				next_odd.append(idx)

	
		print(next_odd)

if __name__ == '__main__':
	nums = [1, 1, 2, 1, 1]
	k = 3

	sol = Solution()
	sol.numberOfSubarrays(nums, k)
