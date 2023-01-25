#!/usr/bin/env python

class Solution(object):
	def maxCoins(self, piles):
		piles.sort(reverse=True)
		
		start = 1
		end = len(piles)
		
		total = 0

		while(start < end):
			total += piles[start]
			start += 2
			end -= 1

		return total


if __name__ == '__main__':
	piles = [2, 4, 1, 2, 7, 8]
	sol = Solution()
	print(sol.maxCoins(piles))
