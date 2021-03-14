#!/usr/bin/env python

from typing import List

class Solution(object):
	def validateStackSequences(self, pushed: List[int], popped: List[int]):
		stk = []
		i = 0

		for val in pushed:
			stk.append(val)

			while stk != [] and stk[-1] == popped[i]:
				stk.pop()
				i += 1

		return stk == []

if __name__ == '__main__':
	pushed = [1, 2, 3, 4, 5]
	popped = [4, 5, 3, 1, 2]

	sol = Solution()
	print(sol.validateStackSequences(pushed, popped))
