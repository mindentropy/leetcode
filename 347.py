#!/usr/bin/env python

from typing import List
import heapq

class Solution(object):
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		freq_hash = dict()

		for val in nums:
			freq_hash[val] = freq_hash.get(val, 0) + 1
		
		return heapq.nlargest(k, freq_hash, freq_hash.get)
		
if __name__ == '__main__':
	nums = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5]
	k = 3 ## K most freq elements

	sol = Solution()
	print(sol.topKFrequent(nums, k))
