#!/usr/bin/env python

class Solution(object):
	def uniqueOccurrences(self, arr):
		"""
		:type arr: List[int]
		:rtype: bool
		"""
		occ_map = {}
		for idx in range(len(arr)):
			if arr[idx] not in occ_map:
				occ_map[arr[idx]] = 1
			else:
				occ_map[arr[idx]] += 1

		val_map = {}
		for val in occ_map.values():
			if val in val_map:
				return False
			else:
				val_map[val] = True

		return True
		
if __name__ == '__main__':

	arr = [1, 2, 2, 1,  3]

	sol = Solution()
	print sol.uniqueOccurrences(arr)
