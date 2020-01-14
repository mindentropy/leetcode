#!/usr/bin/env python

class Solution(object):
	def intersection(self, nums1, nums2):
		op = []
		for num in nums1:
			if num in nums2 and (not num in op):
				op.append(num)
		
		return op

if __name__ == '__main__':
	sol = Solution()
	print sol.intersection([1, 2, 2, 1], [2, 2])
