#!/usr/bin/env python

class Solution(object):
	def checkPossibility(self, nums):

		count = 0
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:

				if count == 1:
					return False

				if (i + 1) == len(nums) - 1:
					return True

				if i == 0:
					nums[i] = nums[i + 1]
					count += 1
				elif i > 0 and nums[i] > nums[i + 1]:
					if nums[i - 1] <= nums[i + 1]:
						nums[i] = nums[i - 1]
						count += 1
					elif nums[i - 1] > nums[i + 1] and (i + 2) < len(nums):
						if nums[i] < nums[i + 2]:
							nums[i + 1] = nums[i]
							count += 1
						else:
							return False
					else:
						return False
							
		return True

if __name__ == '__main__':
	sol = Solution()
	print sol.checkPossibility([1, 2, 4, 5, 3])
