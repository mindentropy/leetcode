#!/usr/bin/env python
import math
from typing import List

class Solution(object):
	def minimumSplits(self, nums: List[int]) -> int:
		arr_cnt = 0
		res = 1

		for idx in range(len(nums)):
			res = math.gcd(res, nums[idx])
			
			if res == 1:
				arr_cnt += 1
				res = nums[idx]

		return arr_cnt


if __name__ == '__main__':
	nums = [12, 6, 3, 14, 8]
	#nums = [4, 12, 6, 14]

	#nums = [17779020, 6955041, 5516067, 479658, 3677378]
	#nums = [8, 2, 3, 6]
	sol = Solution()
	print(sol.minimumSplits(nums))
