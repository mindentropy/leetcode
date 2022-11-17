#!/usr/bin/env python

from typing import List

class Solution(object):
	def generate(self, numRows: int) -> List[List[int]]:
		ans = [0] * numRows
		ans[0] = [1]

		for i in range(1, numRows):
			numarr = [0] * (i + 1)
			j = 0
			while j <= i:
				if j == 0 or j == i:
					numarr[j] = 1
				else:
					numarr[j] = ans[i - 1][j - 1] + ans[i - 1][j]

				j += 1

			ans[i] = numarr

		return ans

if __name__ == '__main__':
	numrows = 6

	sol = Solution()
	print(sol.generate(numrows))
