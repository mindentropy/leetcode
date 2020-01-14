#!/usr/bin/env python
import itertools

class Solution(object):

	def triangle_area(self, p, q, r):
		## Shoelace formula
		return 0.5 * abs(( (q[0] * r[1]) + (p[0] * q[1]) + (r[0] * p[1]) - (r[0] * q[1]) - (p[0] * r[1]) - (q[0] * p[1]) ))

	def largestTriangleArea(self, points):
		max_area = 0

		for idx in itertools.combinations(points, 3):
			area = self.triangle_area(idx[0], idx[1], idx[2])

			if max_area < area:
				max_area = area

		return max_area

if __name__ == '__main__':

	points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
	sol = Solution()
	print sol.largestTriangleArea(points)
