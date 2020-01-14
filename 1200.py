#!/usr/bin/env python

class Solution(object):
	def minimumAbsDifference(self, arr):
		arr.sort()
		arrlen = len(arr)
		
		res = []

		idx = 0
		mindiff = abs(arr[idx+ 1] - arr[idx])

		for idx in range(1, arrlen - 1):
			if mindiff > abs(arr[idx] - arr[idx + 1]):
				mindiff = abs(arr[idx] - arr[idx + 1])

		for idx in range(0, arrlen - 1):
			if mindiff == abs(arr[idx] - arr[idx + 1]):
				res.append([arr[idx], arr[idx + 1]])
			
		return res

if __name__ == '__main__':
	
	arr = [3, 8, -10, 23, 19, -4, -14, 27]

	sol = Solution()
	print sol.minimumAbsDifference(arr)
