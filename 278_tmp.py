#!/usr/bin/env python

def isBadVersion(version):
	pick = 1702766719

	if version >= pick:
		return True
	else:
		return False

class Solution(object):

	def binsearch_good_ver(self, lo, hi):
		mid = lo + (hi - lo)//2
		if isBadVersion(mid) == False:
			return mid
		else:
			return self.binsearch_good_ver(lo, mid - 1)

	def binsearch_bad_ver(self, lo, hi):

		mid = lo + (hi - lo)//2
		if isBadVersion(mid) == True:
			idx2 = mid
			idx1 = self.binsearch_good_ver(lo, mid - 1)
			
			while(idx1 <= idx2):
				if not isBadVersion(idx1):
					idx1 += 1
				else:
					return idx1
		else:
			return self.binsearch_bad_ver(mid + 1, hi)

	def firstBadVersion(self, n):
		return self.binsearch_bad_ver(1, n)

if __name__ == '__main__':

	sol = Solution()
	print(sol.firstBadVersion(2126753390))
