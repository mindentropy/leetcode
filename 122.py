#!/usr/bin/env python

class Solution(object):
	def maxProfit(self, prices):
		profit = 0

		for idx in xrange(len(prices) - 1):
			if prices[idx] < prices[idx + 1]:
				profit += prices[idx + 1] - prices[idx]

		return profit

if __name__ == '__main__':
	
	prices = [1, 2, 3, 4, 5]

	sol = Solution()

	print sol.maxProfit(prices)
