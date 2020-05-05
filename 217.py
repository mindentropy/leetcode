#!/usr/bin/env python

class Solution(object):
	def containsDuplicate(self, nums):
		dup_hash = dict()

		for idx in xrange(len(nums)):
			dup_hash[nums[idx]] = dup_hash.get(nums[idx], 0) + 1

			if dup_hash[nums[idx]] > 1:
				return True


		return False

if __name__ == '__main__':
	sol = Solution()

	print sol.containsDuplicate([1, 2, 3, 1])
