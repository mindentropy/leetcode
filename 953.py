#!/usr/bin/env python

class Solution(object):
	def isAlienSorted(self, words, order):
		rank = dict()

		cnt = 0
		for ch in order:
			rank[ch] = cnt
			cnt += 1

		for idx in xrange(len(words) - 1):
			for x in xrange(idx + 1, len(words)):
				w1 = words[idx]
				w2 = words[x]
				for i in xrange(len(w1)):
					if i >= len(w2):
						return False
					if rank[w1[i]] != rank[w2[i]]:
						if rank[w1[i]] > rank[w2[i]]:
							return False
						elif rank[w1[i]] < rank[w2[i]]:
							break

		return True

if __name__ == '__main__':

#	words = ['kuvp', 'q']
#	order = "ngxlkthsjuoqcpavbfdermiywz"

	words = ['apple', 'app']
	order = "abcdefghijklmnopqrstuvwxyz"

	sol = Solution()
	print sol.isAlienSorted(words, order)
