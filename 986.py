#!/usr/bin/env python

from typing import List

class Solution(object):
	def intervalIntersection(self, firstList: List[List[int]],
		secondList: List[List[int]]) -> List[List[int]]:
			idx1 = 0
			idx2 = 0

			op = []
			while idx1 < len(firstList) and idx2 < len(secondList):
				if firstList[idx1][0] <= secondList[idx2][0]:
					if firstList[idx1][1] < secondList[idx2][0]:
						idx1 += 1
						continue

					st_ed = [0] * 2
					st_ed[0] = secondList[idx2][0]
					if firstList[idx1][1] >= secondList[idx2][1]:
						st_ed[1] = secondList[idx2][1]
						idx2 += 1
					else:
						st_ed[1] = firstList[idx1][1]
						idx1 += 1

					op.append(st_ed)
				elif secondList[idx2][0] <= firstList[idx1][0]:
					
					if secondList[idx2][1] < firstList[idx1][0]:
						idx2 += 1
						continue

					st_ed = [0] * 2
					st_ed[0] = firstList[idx1][0]
					if secondList[idx2][1] >= firstList[idx1][1]:
						st_ed[1] = firstList[idx1][1]
						idx1 += 1
					else:
						st_ed[1] = secondList[idx2][1]
						idx2 += 1

					op.append(st_ed)
			return(op)

if __name__ == '__main__':
	#firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
	#secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

	firstList = [[8, 15]]
	secondList = [[2, 6], [8, 10], [12, 20]]

	sol = Solution()
	print(sol.intervalIntersection(firstList, secondList))
