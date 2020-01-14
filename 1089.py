#!/usr/bin/env python

class Solution(object):
	def duplicateZeros(self, arr):
		endidx = len(arr) - 1
		startidx = 0
		zerocnt = 0

		while startidx < endidx:
			if arr[startidx] == 0:
				endidx -= 1
				zerocnt += 1
			startidx += 1

		
		idx = len(arr) - 1
		print endidx
		print startidx

		if arr[endidx] == 0 and endidx > startidx:
			arr[idx] = 0
			idx -= 1
			endidx -= 1

		while endidx >= 0:
			if arr[endidx] == 0:
				arr[idx] = arr[idx - 1] = 0
				idx -= 1
			else:
				arr[idx] = arr[endidx]

			idx -= 1
			endidx -= 1 

		print arr

if __name__ == '__main__':
	sol = Solution()
	arr2 = [1, 0, 2, 3, 0, 4, 5, 0]
	arr1 = [8, 4, 5, 0, 0, 0, 0, 7]

	arr3 = [1, 5, 2, 0, 6, 8, 0, 6, 0]
	sol.duplicateZeros(arr2)
