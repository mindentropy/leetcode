#!/usr/bin/env python

class Solution(object):
	def minAddToMakeValid(self, S: str) -> int:
		stk = []
		cnt = 0

		for val in S:
			if val == ')':
				if stk == []:
					cnt += 1
				else:
					if stk[-1] == '(':
						stk.pop()
					else:
						stk.push(val)
			elif val == '(':
				stk.append(val)

		return cnt + len(stk)
				

if __name__ == '__main__':

	sol = Solution()

	print(sol.minAddToMakeValid('()))(('))
