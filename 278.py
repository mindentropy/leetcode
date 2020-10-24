#!/usr/bin/env python

def isBadVersion(version):
	pick = 4

	if version >= pick:
		return True
	else:
		return False

class Solution(object):

	def binsearch(self, lo, hi):
		
		if lo < hi:
			mid = (lo + hi)//2
			if isBadVersion(mid) == True:
				return self.binsearch(lo, mid - 1)
			else:
				return self.binsearch(mid, hi)
		else:
			##TODO: Analyse what happens if it meets
				

	def firstBadVersion(self, n):
		return self.binsearch(1, n)

if __name__ == '__main__':

	sol = Solution()
	print(sol.firstBadVersion(5))
