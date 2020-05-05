#!/usr/bin/env python

from typing import List

class Solution(object):
	def lemonadeChange(self, bills: List[int]) -> bool:
		change = 0
		bill_map = dict()

		bill_map[5] = 0
		bill_map[10] = 0
		bill_map[20] = 0

		for val in bills:
			if val == 5:
				bill_map[5] += 1
			elif val == 10:
				if bill_map[5] > 0:
					bill_map[5] -= 1
					bill_map[10] += 1
				else:
					return False
			elif val == 20:
				if (bill_map[10] > 0 and bill_map[5] > 0):
					bill_map[10] -= 1
					bill_map[5] -= 1
					bill_map[20] += 1
				elif (bill_map[5]) >= 3:
					bill_map[5] -= 3
					bill_map[20] += 1
				else:
					return False
					
		return True

if __name__ == '__main__':
	sol = Solution()
	print(sol.lemonadeChange([5, 5, 5, 10, 20]))
