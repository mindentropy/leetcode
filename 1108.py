#!/usr/bin/env python

class Solution(object):
	def defangIPaddr(self, address: str) -> str:
		defangstr = ""

		for ch in address:
			if ch == '.':
				defangstr +='[.]'
			else:
				defangstr += ch

		return defangstr
		
if __name__ == '__main__':
	addr = '1.1.1.1'

	sol = Solution()

	print(sol.defangIPaddr(addr))
