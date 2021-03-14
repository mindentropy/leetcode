#!/usr/bin/env python

class Solution(object):
	
	def reverseParentheses(self, s: str) -> str:
		idx_stk = []
		val_stk = []
		op = []

		i = 0
		j = 0

		while i < len(s):
			if s[i] == '(':
				idx_stk.append(j)
			elif s[i] == ')':
				start = idx_stk.pop()
				end = j
				
				
				lst = op[start:end]
				lst = lst[len(lst)::-1]
				if op[0:start] != None:
					op = op[0:start] + lst
				else:
					op = lst
			else:
				op += s[i]
				j += 1

			i += 1
		
		opstr=""
		return opstr.join(op)

if __name__ == '__main__':
	s = '(u(love)i)'
	sol = Solution()
	print(sol.reverseParentheses(s))
