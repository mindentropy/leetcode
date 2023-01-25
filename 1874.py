#!/usr/bin/env python

class Solution(object):
	def minProductSum(self, nums1, nums2):
		nums1.sort()
		nums2.sort(reverse=True)
		
		total = 0

		for idx in range(len(nums1)):
			total += nums1[idx] * nums2[idx]

		return total

if __name__ == '__main__':
	nums1 = [5, 3, 4, 2]
	nums2 = [4, 2, 2, 5]

	sol = Solution()
	print(sol.minProductSum(nums1, nums2))
