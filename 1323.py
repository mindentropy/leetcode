#!/usr/bin/env python

class Solution(object):
	def maximum69Number(self, num:int) -> int:
		arr = []
		op = 0

		if num == 9999:
			return num

		while(num):
			arr.append(num%10)
			num = int(num/10)

		idx = len(arr) - 1
		while idx >= 0:
			if arr[idx] == 6:
				arr[idx] = 9
				break
			idx -= 1

		idx = len(arr) - 1
		while idx >= 0:
			op *= 10
			op += arr[idx]
			idx -= 1

		return op

if __name__ == '__main__':
	num = 9999
	sol = Solution()
	print(sol.maximum69Number(num))
