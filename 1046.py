#!/usr/bin/env python

import heapq

class Solution(object):
	def lastStoneWeight(self, stones):
		for idx in range(len(stones)):
			stones[idx] = -stones[idx]
		
		heapq.heapify(stones)
		while len(stones) != 1 and len(stones) != 0:
			max1 = heapq.heappop(stones)
			max2 = heapq.heappop(stones)
			print stones

			if max1 != max2:
				heapq.heappush(stones, -abs(max1 - max2))

		if len(stones) == 1:
			return -stones[0]
		else:
			return 0
		
if __name__ == '__main__':
	stones = [2, 7, 4, 1, 8, 1]
	sol = Solution()
	print sol.lastStoneWeight(stones)
