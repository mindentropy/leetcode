#!/usr/bin/env python

class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		maxcnt = 0
		onecnt = 0

		for val in nums:
			if val == 0:
				if maxcnt < onecnt:
					maxcnt = onecnt
				onecnt = 0
			elif val == 1:
				onecnt += 1

		if onecnt > maxcnt:
			maxcnt = onecnt

		return maxcnt

if __name__ == '__main__':
	sol = Solution()
	print sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
