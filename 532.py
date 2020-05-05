#!/usr/bin/env python

class Solution(object):
	def findPairs(self, nums, k):

		pairs = []

		nums.sort()

		for i in range(len(nums) - 1):
			j = i + 1
			while j < len(nums):
				if abs(nums[i] - nums[j]) == k:
					#print '(%d,%d)' % (nums[i], nums[j])
					if not (nums[i], nums[j]) in pairs:
						pairs.append((nums[i], nums[j]))
				elif abs(nums[i] - nums[j]) > k:
					break

				j = j + 1

		#print pairs
		return len(pairs)

if __name__ == '__main__':
	sol = Solution()
	print sol.findPairs([1, 3, 1, 5 , 4], 0)
