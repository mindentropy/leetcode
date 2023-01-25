#!/usr/bin/env python

class Solution(object):
	def minimumSum(self, num: int) -> int:
		arr = []

		while num:
			arr.append(num%10)
			num = int(num / 10)

		arr.sort()
		
		return ((arr[0] * 10 + arr[2]) + (arr[1] * 10 + arr[3]))

if __name__ == '__main__':
	sol = Solution()

	print(sol.minimumSum(4009))
