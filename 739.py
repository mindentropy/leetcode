#!/usr/bin/env python

from typing import List

class Solution(object):
#	def dailyTemperatures(self, T: List[int]) -> List[int]:
#		op = [0] * len(T)
#
#		maxval = (0,0)
#
#		for i in range(len(T)):
#			if maxval[0] > i and maxval[1] > T[i]:
#				j = i
#				while j < maxval[0]:
#					if T[j] > T[i]:
#						op[i] = j - i
#						break
#
#					j += 1
#
#				if j == maxval[0]:
#					op[i] = j - i
#					maxval = (0, 0)
#			else:
#				j = i + 1
#				while j < len(T):
#					if T[j] > T[i]:
#						op[i] = j - i
#						maxval = (j, T[j])
#						break
#					j += 1
#
#		return op

#	def dailyTemperatures(self, T: List[int]) -> List[int]:
#		op = [0] * len(T)
#		idx_max_val = 30001
#		next_val = [idx_max_val]  * 101
#
#		i = len(T) - 1
#		while i >= 0:
#			warmer_idx = idx_max_val
#
#			for val in list(range(T[i] + 1, 101)):
#				if next_val[val] < warmer_idx:
#					warmer_idx = next_val[val]
#			
#			if warmer_idx < idx_max_val:
#				op[i] = warmer_idx - i
#				
#			next_val[T[i]] = i
#
#			i -= 1
#
#		return op
					
	def dailyTemperatures(self, T: List[int]) -> List[int]:
		op = [0] * len(T)
		stk = []

		i = len(T) - 1

		while i >= 0:

			if stk == []:
				op[i] = 0
				stk.append(i)
			else:
				while stk != [] and T[stk[-1]] <= T[i]:
					stk.pop()

				if stk == []:
					stk.append(i)
					op[i] = 0
				else:
					op[i] = stk[-1] - i
					stk.append(i)
			
			i -= 1

		return op


if __name__ == '__main__':
	T = [73, 74, 75, 71, 69, 72, 76, 73]
	sol = Solution()
	print(sol.dailyTemperatures(T))
