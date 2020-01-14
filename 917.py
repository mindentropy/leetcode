#!/usr/bin/env python

class Solution(object):
	def reverseOnlyLetters(self, S):
		S = list(S)
		startidx = 0
		endidx = len(S) - 1
		
		if startidx == endidx:
			return ''.join(S)
		
		while startidx <= endidx:
			while not S[startidx].isalpha():
				startidx += 1

				if startidx == len(S):
					break

			while not S[endidx].isalpha():
				endidx -= 1

				if endidx == 0:
					break

			if startidx >= endidx:
				break
			
			S[startidx], S[endidx] = S[endidx], S[startidx]

			startidx += 1
			endidx -= 1

		return ''.join(S)
	
if __name__ == '__main__':
	sol = Solution()

	print sol.reverseOnlyLetters('7_28]')
