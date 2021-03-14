#!/usr/bin/env python

from typing import List

class Solution(object):
	def buildArray(self, target: List[int], n: int) -> List[str]:
		
		cnt = 1
		op = []

		i = 0
#		while i < len(target):
#			if target[i] == cnt:
#				op.append("Push")
#				cnt += 1
#			else:
#				while target[i] != cnt:
#					op.append("Push")
#					op.append("Pop")
#					cnt += 1
#
#				continue
#
#			i += 1

		while i < len(target):
			while target[i] != cnt:
				op.append("Push")
				op.append("Pop")
				cnt += 1

			op.append("Push")
			cnt += 1
			i += 1

		return op

if __name__ == '__main__':
	
	target = [1, 3]
	sol = Solution()
	print(sol.buildArray(target, 4))
