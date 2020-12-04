#!/usr/bin/env python

class Solution(object):
	def maxSatisfied(self, customers, grumpy, X):
		totalcnt = 0

		for idx in range(len(customers)):
			if grumpy[idx] == 0:
				totalcnt += customers[idx]
			
			idx += 1

		idx = 0
		while idx < X:
			if grumpy[idx] == 1:
				totalcnt += customers[idx]

			idx += 1
	
		maxcnt = totalcnt

		while idx < len(customers):
			if grumpy[idx - X ] == 1:
				totalcnt -= customers[idx - X]

			if grumpy[idx] == 1:
				totalcnt += customers[idx]
		
			if maxcnt < totalcnt:
				maxcnt = totalcnt

			idx += 1
		
		return maxcnt

if __name__ == '__main__':
	customers = [1, 0, 1, 2, 1, 1, 7, 5]
	grumpy 	  = [0, 1, 0 ,1, 0, 1, 0, 1]
	X = 3

	#customers = [3]
	#grumpy 	  = [1]
	#X = 1

	sol = Solution()
	print(sol.maxSatisfied(customers, grumpy, X))
