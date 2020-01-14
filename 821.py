#!/usr/bin/env python

class Solution(object):
	def shortestToChar(self, S, C):
		dist = [10001] * len(S)
		lidx = 0
		ridx = 0

		for idx in range(len(S)):
			if S[idx] == C:
				dist[idx] = 0
				lidx = idx - 1
				ridx = idx + 1
				d = 1

				while lidx >= 0 and S[lidx] != C and dist[lidx] > d:
					dist[lidx] = d
					d += 1
					lidx -= 1

				d = 1
				while ridx < len(S) and S[ridx] != C :
					dist[ridx] = d
					d += 1
					ridx += 1

		return dist

if __name__ == '__main__':
	S = 'loveleetcode'
	C = 'e'
	sol = Solution()
	print sol.shortestToChar(S, C)
