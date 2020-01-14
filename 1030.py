#!/usr/bin/env python

class Solution(object):
	def allCellsDistOrder(self, R, C, r0, c0):
		result = []
		dist = dict()
		
		max_dst = -1

		for ridx in range(R):
			for cidx in range(C):
				d = abs(r0 - ridx) + abs(c0 - cidx)
				if d > max_dst:
					max_dst = d

				if d not in dist:
					dist[d] = [[ridx, cidx]]
				else:
					dist[d].append([ridx, cidx])
		
		for val in range(max_dst + 1):
			for val in dist[val]:
				result.append(val)

		return result

if __name__ == '__main__':
	sol = Solution()
	print sol.allCellsDistOrder(2, 3, 1, 2)
