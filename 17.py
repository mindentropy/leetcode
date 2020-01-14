#!/usr/bin/env python

class Solution(object):
	def __init__(self):
		self.phone = {
					'2': ['a', 'b', 'c'],
					'3': ['d', 'e', 'f'],
					'4': ['g', 'h', 'i'],
					'5': ['j', 'k', 'l'],
					'6': ['m', 'n', 'o'],
					'7': ['p', 'q', 'r', 's'],
					'8': ['t', 'u', 'v'],
					'9': ['x', 'y', 'z']
				}

	def gen_letter_combi(self, sol, digits):

		if len(digits) == 0:
			
		else:
			for k in range(len(digits)):
				if digits[k] not in sol:
					sol += digits[k]
					self.gen_letter_combi(sol, digits[1:])
					del sol[-1]

	def print_combi(self, sol):
		for val in sol:
			print val,

		print ""
		
	def letterCombinations(self, digits):
		elements = []

		sol = []

		self.gen_letter_combi(sol, digits)
	
if __name__ == '__main__':
	sol = Solution()
	sol.letterCombinations('234')
