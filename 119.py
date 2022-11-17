#!/usr/bin/env python

from typing import List

class Solution(object):
	def getRow(self, rowIndex: int) -> List[int]:

		if rowIndex == 0:
			return [1]
		
		numarr = [0] * (rowIndex)
		for i in range(1, rowIndex):
			j = 0
			while j < (i + 1):
				if j == 0 or j == i:
					numarr[j] = 1
				else:
					numarr[j] = numarr[j - 1] + numarr[j]

				j += 1

			prevarr = numarr
			print(numarr)

if __name__ == '__main__':
	sol = Solution()
	sol.getRow(4)
