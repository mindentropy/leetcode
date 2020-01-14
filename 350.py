#!/usr/bin/env python

class Solution(object):
	def intersect(self, nums1, nums2):
		op = []
		for num in nums1:
			for j in range(len(nums2)):
				if num == nums2[j] and nums2[j] != '':
					op.append(num)
					nums2[j] = ''
					break
				j += 1
		
		return op

if __name__ == '__main__':
	sol = Solution()
	print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
