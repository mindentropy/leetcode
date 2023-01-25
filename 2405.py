#!/usr/bin/env python

class Solution(object):
	def partitionString(self, s: str) -> int:
		arr = [0] * 27
		cnt = 0
		for val in s:
			if arr[ord(val) - 118] == 1:
				cnt += 1
				arr = [0] * 27
			else:
				arr[ord(val) - 118] = 1

		return cnt + 1
				

if __name__ == '__main__':
	s = 'abacaba'
	sol = Solution()
	print(sol.partitionString(s))
