#!/usr/bin/env python

class Solution1(object):
	def nextGreaterElement(self, nums1, nums2):
		
		len1 = len(nums1)
		len2 = len(nums2)

		result = [-1] * len1

		for idx in range(len1):
			val = nums1[idx]
			
			idx2 = 0
			for idx2 in range(len2):
				if nums2[idx2] == val:
					break

			while(idx2 < len2):
				if nums2[idx2] > val:
					result[idx] = nums2[idx2]
					break

				idx2 += 1
			
		return result

class Solution2(object):
	def nextGreaterElement(self, nums1, nums2):
		
		len1 = len(nums1)
		len2 = len(nums2)

		result = [-1] * len1
		
		nummap = dict()

		for idx in range(len2):
			nummap[nums2[idx]] = idx

		for idx in range(len1):
			val = nums1[idx]
			
			idx2 = nummap[val]
			while(idx2 < len2):
				if nums2[idx2] > val:
					result[idx] = nums2[idx2]
					break

				idx2 += 1
			
		return result

class Solution(object):
	def nextGreaterElement(self, nums1, nums2):
		nummap = dict()

		result = [-1] * len(nums1)

		ngre = []

		for val in nums2:
			while len(ngre) != 0 and ngre[-1] < val:
				nummap[ngre.pop()] = val
			
			ngre.append(val)

		idx = 0
		for idx in range(len(nums1)):
			if nums1[idx] in nummap:
				result[idx] = nummap[nums1[idx]]

		return result
		
if __name__ == '__main__':
	sol = Solution()

	nums1 = [4, 1, 2]
	nums2 = [1, 3, 4, 2]

	print sol.nextGreaterElement(nums1, nums2)
