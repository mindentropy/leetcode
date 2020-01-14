#!/usr/bin/env python

class Solution(object):
	def rotatedDigits(self, N):

		numcnt = 0
		for val in xrange(1, N + 1):
			numstr = list(str(val))
			changeflag = False
			for idx in xrange(len(numstr)):
				if numstr[idx] in [ '1', '0', '8']:
					continue
				elif numstr[idx] in ['2', '5', '6', '9']:
					changeflag = True
				else:
					changeflag = None
					break

			if changeflag == True:
				numcnt += 1

		return numcnt

				
if __name__ == '__main__':
	sol = Solution()

	print sol.rotatedDigits(857)
