#!/usr/bin/env python

class Solution(object):
	def __init__(self):
		self.final_sol = []

	def gen_permutation(self, i, sol, S):
		if len(sol) == len(S):
			self.final_sol.append(''.join(sol))
		else:
			for k in range(0, 2):
				if k == 1:
					if S[i].islower():
						sol += S[i].upper()
					else:
						sol += S[i].lower()
				else:
					sol += S[i]

				self.gen_permutation(i + 1, sol, S)
				del sol[-1]

				if not S[i].isalpha():
					break

	def letterCasePermutation(self, S):
		sol = []
		self.gen_permutation(0, sol, S)
		return self.final_sol

if __name__ == '__main__':
	s = 'C'
	sol = Solution()
	print sol.letterCasePermutation(s)

