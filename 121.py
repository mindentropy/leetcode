#!/usr/bin/env python

#class Solution(object):
#	def maxProfit(self, prices):
#		maxprofit = 0
#		for buyidx in xrange(len(prices) - 1):
#			for sellidx in xrange(buyidx, len(prices)):
#				profit = prices[sellidx] - prices[buyidx]
#				if maxprofit < profit:
#					maxprofit = profit
#
#
#		return maxprofit

class Solution(object):
	def maxProfit(self, prices):
		minprice = 10000000
		maxprofit = 0

		for idx in xrange(len(prices)):
			if prices[idx] < minprice:
				minprice = prices[idx]
			else:
				if (prices[idx] - minprice) > maxprofit:
					maxprofit = prices[idx] - minprice

		return maxprofit

if __name__ == '__main__':
	prices = [7, 1, 5, 3, 6, 4]

	sol = Solution()
	print sol.maxProfit(prices)
