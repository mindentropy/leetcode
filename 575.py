#!/usr/bin/env python

class Solution(object):
	def distributeCandies(self, candies):
		cfreq = {}

		for val in candies:
			cfreq[val] = cfreq.get(val, 0) + 1
		
		totalcandies = len(candies) >> 1

		maxcandies = 0

		## Get all kinds of candies with the lowest count
		for val in cfreq:
			if cfreq[val]:
				maxcandies += 1
				cfreq[val] -= 1

			if maxcandies == totalcandies:
				break

		return maxcandies

if __name__ == '__main__':
	candies = [1, 1, 2, 3]

	sol = Solution()
	print sol.distributeCandies(candies)
