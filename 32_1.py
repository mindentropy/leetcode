#!/usr/bin/env python

class Solution(object):
	def longestValidParentheses(self, s):
		total_len = len(s)
		
		idx = 0
		balance = 0
		max_seq = 0

		seq = 0
		while total_len:

			if s[idx] == '(':
				balance += 1
			elif s[idx] == ')':
				balance -= 1
			
			if balance > 1 or balance < 0:
				seq = 0
				if balance > 1:
					balance = 1
				else:
					balance = 0
			elif balance == 0:
				seq += 2

				if max_seq < seq:
					max_seq = seq

			total_len -= 1
			idx += 1

		return max_seq

if __name__ == '__main__':

	sol = Solution()
	print(sol.longestValidParentheses('(()'))
