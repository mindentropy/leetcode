#!/usr/bin/env python

class Solution(object):
	def numberOfLines(self, widths, S):
		widthcnt = 0
		linewidth = 0
		linecnt = 1

		for ch in S:
			widthcnt = (widths[ord(ch) - 97])

			if linewidth + widthcnt > 100:
				linecnt += 1
				linewidth = widthcnt
			else:
				linewidth += widthcnt

		
		return [linecnt, linewidth]

if __name__ == '__main__':
	
	widths = [10] * 26
	S = 'abcdefghijlkmnopqrstuvwxyz'

	sol = Solution()
	print sol.numberOfLines(widths, S)
