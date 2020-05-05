#!/usr/bin/env python

from math import gcd

class Solution(object):
	def hasGroupsSizeX(self, deck):
		deck_map = dict()

		for val in deck:
			deck_map[val] = deck_map.get(val, 0) + 1

		a = 0
		if len(deck_map.keys()) > 2:
			key, a = deck_map.popitem()
		
		for key, val in deck_map.items():
			gcdval = gcd(a, val)

			if gcdval < 2:
				return False

			a = gcdval


		return True


if __name__ == '__main__':
	sol = Solution()
	print(sol.hasGroupsSizeX([1, 1, 1, 2, 2]))
