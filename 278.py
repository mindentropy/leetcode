#!/usr/bin/env python

def isBadVersion(version):
	pick = 4

	if version >= pick:
		return True
	else:
		return False

class Solution(object):

	def binsearch(self, lo, hi):
		if lo > hi:
			return lo
			## TODO: Analyse what happens if it meets
			## lo == hi and isBadVersion(mid) == False Then what will I return??
		else:
			mid = (lo + hi)//2
			if isBadVersion(mid) == False:
				return self.binsearch(mid + 1, hi)
			elif isBadVersion(mid) == True:
				return self.binsearch(lo, mid - 1)

	def firstBadVersion(self, n):
		return self.binsearch(1, n)

if __name__ == '__main__':

	sol = Solution()
	print(sol.firstBadVersion(5))
