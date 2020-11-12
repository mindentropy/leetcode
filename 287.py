#!/usr/bin/env python

class Solution(object):
#	def findDuplicate(self, nums):
#		nums.sort()
#		
#		prev = nums[0]
#
#		for val in nums[1:]:
#			if prev == val:
#				return prev
#			else:
#				prev = val

	def findDuplicate(self, nums):
		slowidx = 0
		fastidx = 0

		slowidx = nums[slowidx]
		fastidx = nums[fastidx]
		while True:
			slowidx = nums[slowidx]
			fastidx = nums[nums[fastidx]]

			if slowidx == fastidx:
				break

		slowidx = nums[0]
		while True:
			if fastidx == slowidx:
				return slowidx

			fastidx = nums[fastidx]
			slowidx = nums[slowidx]

if __name__ == '__main__':
	nums = [1, 3, 4, 2, 2]
	sol = Solution()
	print(sol.findDuplicate(nums))
