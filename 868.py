#!/usr/bin/env python

class Solution(object):
	def binaryGap(self, N):
		startidx = 0
		endidx = 0
		
		maxgap = 0

		while startidx < 32:
			if N & (1<<startidx):
				endidx = startidx + 1
				while endidx < 32:
					if N & (1<<endidx):
						if maxgap < (endidx - startidx):
							maxgap = endidx - startidx 
						break
					endidx += 1
			startidx += 1
		
		return maxgap

if __name__ == '__main__':
	sol = Solution()
	print sol.binaryGap(15)
