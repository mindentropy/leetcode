#!/usr/bin/env python

from typing import List

class Solution(object):
	def partitionLabels(self, S: str) -> List[int]:
		
		freq = {}
		hold_map = {}
		
		part_map_cnt = []
		cnt = 0

		for val in S:
			freq[val] = freq.get(val, 0) + 1
			
		for val in S:
			if val not in hold_map:
				hold_map[val] = freq[val] - 1
			else:
				hold_map[val] -= 1

			cnt += 1

			if hold_map[val] == 0:
				del(hold_map[val])

			if hold_map == {}:
				part_map_cnt.append(cnt)
				cnt = 0

		return part_map_cnt


if __name__ == '__main__':
	S = "ababcbacadefegdehijhklij"

	sol = Solution()
	print(sol.partitionLabels(S))
