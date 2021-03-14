#!/usr/bin/env python

class Solution(object):
	def scoreOfParentheses(self, S: str) -> int:
		stk = [0]
	
		for val in S:
			if val == '(':
				stk.append(0)
			elif val == ')':
				val = stk.pop()
				if val == 0:
					stk[-1] += 1
				else:
					stk[-1] += 2 * val

		return stk[-1]

if __name__ == '__main__':
	sol = Solution()

	print(sol.scoreOfParentheses('(()(()))'))
