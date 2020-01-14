#!/usr/bin/env python

class Solution(object):
	def removeOuterParentheses(self, S):
		startpos = endpos = 0
		bal = 0

		string = ""
		for ch in S:
			if ch == '(':
				bal += 1
			elif ch == ')':
				bal -= 1
			
			if bal == 0:
				#decomposed_str.extend([S[startpos:endpos+1]])
				string += S[startpos+1:endpos]
				startpos = endpos + 1

			endpos += 1
		
		return string

if __name__ == '__main__':
#	inpstr = '(()())(())'
	inpstr = '(()())(())(()(()))'
#	inpstr = '()()'

	print(inpstr)
	sol = Solution()
	print(sol.removeOuterParentheses(inpstr))
