#!/usr/bin/env python

class Solution(object):
	def findSpecialInteger(self, arr):
		freq = dict()

		maxrepeatcnt = 0

		maxcount = 0.25 * len(arr)

		for idx in xrange(len(arr)):
			freq[arr[idx]] = freq.get(arr[idx], 0) + 1

			if freq[arr[idx]] > maxrepeatcnt:
				maxrepeatcnt = freq[arr[idx]]
				if maxrepeatcnt > maxcount:
					return arr[idx]


if __name__ == '__main__':
	arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]

	sol = Solution()
	print sol.findSpecialInteger(arr)
