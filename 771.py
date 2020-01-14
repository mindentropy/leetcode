#!/usr/bin/env python

class Solution(object):
	def numJewelsInStones(self, J, S):
		"""
		:type J: str
		:type S: str
		:rtype: int
		"""

		jewel_count = 0

		for jewel in J:
			for stone in S:
				if jewel == stone:
					jewel_count += 1


		return jewel_count

if __name__ == '__main__':
	sol = Solution()
	
	J = 'aA'
	S = 'aAAbbbb'

	print(sol.numJewelsInStones(J, S))
