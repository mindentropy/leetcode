#!/usr/bin/env python

class Solution(object):
	def uncommonFromSentences(self, A, B):
		strhash = dict()
		op = []

		for word in A.split():
			if word in strhash:
				strhash[word] += 1
			else:
				strhash[word] = 0

		for word in B.split():
			if word in strhash:
				strhash[word] += 1
			else:
				strhash[word] = 0

		for key in strhash:
			if strhash[key] == 0:
				op.append(key)

		return op

if __name__ == '__main__':

	A = 'this apple is sweet'
	B = 'this apple is sour'

	sol = Solution()
	print sol.uncommonFromSentences(A, B)
