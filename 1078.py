#!/usr/bin/env python

class Solution(object):
	def findOcurrences(self, text, first, second):
		wordlst = text.split(' ')
		
		idx = 0
		
		result = []
		for idx in range(len(wordlst)):
			if second == wordlst[idx]:
				if (idx - 1) >= 0 and wordlst[idx - 1] == first and (idx + 1) < len(wordlst):
					result.append(wordlst[idx + 1])

		return result

if __name__ == '__main__':
	text = 'we will we will rock you'
	first = 'we'
	second = 'will'

	sol = Solution()
	print sol.findOcurrences(text, first, second)
