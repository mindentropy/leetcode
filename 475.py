#!/usr/bin/env python


class Solution(object):
	def findRadius(self, houses, heaters):
		heaters.sort()
		houses.sort()

		return 1

if __name__ == '__main__':
	sol = Solution()
	print(sol.findRadius([1,2,3], [2]))
