#!/usr/bin/env python
from collections import OrderedDict

class Solution(object):
	def relativeSortArray(self, arr1, arr2):
		result = [0] * len(arr1)

		arr2_dict = OrderedDict()

		for val in arr2:
			arr2_dict[val] = 1

		
		result1 = []
		for val in arr1:
			if val not in arr2_dict:
				result1.append(val)
			else:
				arr2_dict[val] += 1

		result1.sort()

		idx = 0
		for val in arr2:
			count = arr2_dict[val] - 1 
			while count > 0:
				result[idx] = val
				idx += 1
				count -= 1


		for val in result1:
			result[idx] = val
			idx += 1

		return result
		

if __name__ == '__main__':


	arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
	arr2 = [2,42,38,0,43,21]

	sol = Solution()
	print sol.relativeSortArray(arr1, arr2)
