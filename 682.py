#!/usr/bin/env python

class Solution(object):
	def calPoints(self, ops):
		stk = []
		total = 0

		for op in ops:
			if op == 'D':
				stk.append(stk[-1] * 2)
			elif op == 'C':
				stk.pop()
			elif op == '+':
				stk.append(stk[-1] + stk[-2])
			else:
				stk.append(int(op))

		for val in stk:
			total += val

		return total

if __name__ == '__main__':
	ops = ["5","-2","4","C","D","9","+","+"]

	sol = Solution()
	print sol.calPoints(ops)
