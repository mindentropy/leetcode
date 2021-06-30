#!/usr/bin/env python
from typing import List

class Solution(object):
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		min_costs = [0] * (len(cost) + 1)
		#Min cost for steps 0 and 1 is 0.

		for i in range(2, len(cost) + 1):
							## min(one step, two step)
			min_costs[i] = min(min_costs[i - 1] + cost[i - 1], \
								min_costs[i - 2] + cost[i - 2])

		return min_costs[-1]

if __name__ == '__main__':
	cost = [10, 15, 20]
	sol = Solution()
	print(sol.minCostClimbingStairs(cost))
