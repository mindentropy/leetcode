#!/usr/bin/env python

class Solution(object):
	def sortArrayByParityII(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		
		parity_arr = [None] * len(A)

		count = 0	
		for idx, val in enumerate(A):
			if val & 1 == 0:
				parity_arr[count] = val
				count = count + 2

		count = 1
		for idx, val in enumerate(A):
			if val & 1 == 1:
				parity_arr[count] = val
				count = count + 2
			
		return parity_arr

if __name__ == '__main__':
	A = [2,3,1,1,4,0,0,4,3,3]

	sol = Solution()
	print sol.sortArrayByParityII(A)

