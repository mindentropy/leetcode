#!/usr/bin/env python

class Solution(object):
	def canThreePartsEqualSum(self, A):

		if sum(A) % 3 != 0:
			return False

		partsum = sum(A) // 3
		
		idx = 0
		partcnt = 0

		for i in xrange(3):

			sumval = 0
			
			while idx != len(A):
				sumval += A[idx]
				idx += 1

				if sumval == partsum:
					partcnt += 1
					break

		if partcnt == 3:
			return True
		else:
			return False
		
if __name__ == '__main__':
	arr1 = [0,2,1,-6,6,-7,9,1,2,0,1]
	arr2 = [3,3,6,5,-2,2,5,1,-9,4]
	arr3 = [0,2,1,-6,6,7,9,-1,2,0,1]
	sol = Solution()
	print sol.canThreePartsEqualSum(arr1)
