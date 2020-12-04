#!/usr/bin/env python

class Solution(object):
	def merge(self, nums1, m, nums2, n):
		idx1 = 0
		idx2 = m
		idx4 = 0
		
		if n == 0:
			return

		while idx1 < m and m < len(nums1):
			if nums1[idx1] > nums2[idx4]:
				idx3 = idx2
				while idx3 > idx1:
					nums1[idx3] = nums1[idx3 - 1]
					idx3 -= 1
				nums1[idx1] = nums2[idx4]
				idx2 += 1
				idx4 += 1
				m += 1

			idx1 += 1

		while idx4 < n:
			nums1[idx2] = nums2[idx4]
			idx4 += 1
			idx2 += 1

		print(nums1)

if __name__ == '__main__':
	nums1 = [2, 0]
	nums2 = [1]

	sol = Solution()
	sol.merge(nums1, 1, nums2, 1)
