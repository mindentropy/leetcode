#!/usr/bin/env python

class Solution(object):
	def backspaceCompare(self, S: str, T: str) -> bool:
		stk1 = list()
		stk2 = list()

		for idx in range(len(S)):
			if S[idx] != '#':
				stk1.append(S[idx])
			else:
				if len(stk1):
					stk1.pop()

		for idx in range(len(T)):
			if T[idx] != '#':
				stk2.append(T[idx])
			else:
				if len(stk2):
					stk2.pop()

		if ''.join(stk1) == ''.join(stk2):
			return True
		else:
			return False

if __name__ == '__main__':
	sol = Solution()
	print(sol.backspaceCompare('ab#c', 'ad#c'))
