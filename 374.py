#!/usr/bin/env python

def guess(num):
	pick = 7
	
	if pick < num:
		return -1
	elif pick > num:
		return 1
	elif pick == num:
		return 0
	
class Solution(object):
	def guess_bin_search(self, lo, hi):
		mid = (lo + hi)//2

		if guess(mid) == 0:
			return mid
		elif guess(mid) == 1:
			return self.guess_bin_search(mid + 1, hi)
		elif guess(mid) == -1:
			return self.guess_bin_search(lo, mid - 1)

	def guessNumber(self, n):
		return self.guess_bin_search(1, n)

if __name__ == '__main__':
	sol = Solution()
	print(sol.guessNumber(7))
