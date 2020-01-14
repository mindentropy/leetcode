#!/usr/bin/env python

class Solution(object):
	def distanceBetweenBusStops(self, distance, start, destination):
		n = len(distance)

		cdist = 0
		s = start
		while s != destination:
			cdist += distance[s]

			s = (s + 1) % n

		print cdist

		acdist = 0
		d = destination
		while start != d:
			acdist += distance[d]
			d = (d + 1) % n
			
		print acdist

		return min(cdist, acdist)

if __name__ == '__main__':
	distance = [1, 2, 3, 4]
	sol = Solution()
	print sol.distanceBetweenBusStops(distance, 0, 1)
