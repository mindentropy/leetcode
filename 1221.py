#!/usr/bin/env python

class Solution(object):
	def balancedStringSplit(self, s):
		bal = 0
		bal_cnt = 0
		start_ch = None

		for ch in s:
			if start_ch == None:
				bal += 1
				start_ch = ch
			else:
				if start_ch != ch:
					bal -= 1
				else:
					bal += 1

				if bal == 0:
					bal_cnt += 1
					start_ch = None

		return bal_cnt

if __name__ == '__main__':
	sol = Solution()
	print sol.balancedStringSplit('RLRRLLRLRL')
	print sol.balancedStringSplit('RLLLLRRRLR')
	print sol.balancedStringSplit('LLLLRRRR')
