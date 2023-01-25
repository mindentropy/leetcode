#!/usr/bin/env python

class Solution(object):
		
	def minimumSwaps(self, nums):

		if len(nums) == 1:
			return 0
		
		l_idx = 0
		s_idx = 0

		for idx in range(len(nums)):
			if nums[idx] >= nums[l_idx]:
				l_idx = idx

			if nums[idx] < nums[s_idx]:
				s_idx = idx
		
		swp_cnt = 0
		if l_idx < s_idx:
			s_idx -= 1 ## Smaller index in the way. Reduce the index by one as we
						## pass through

		swp_cnt += len(nums) - l_idx - 1 ## Diff between end and the current index

		return swp_cnt + s_idx ## Add the s_idx to the swap count

if __name__ == '__main__':
	sol = Solution()

	nums = [3, 4, 5, 5, 3, 1]
	print(sol.minimumSwaps(nums))
