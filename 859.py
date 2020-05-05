#!/usr/bin/env python

class Solution(object):
	def buddyStrings(self, A, B):
		swp_cnt = 0

		if len(A) != len(B):
			return False

		## Note: Got the set wrong as I was not familiar with it.
		## len(set(A)) < len(A) for eg: A = ABAB B= ABAB, then set(A) < len(A)
		if A == B and len(set(A)) < len(A):
			return True

		lst_pos = []

		for idx in xrange(len(A)):
			if A[idx] != B[idx]:
				lst_pos.append(idx)
				if len(lst_pos) > 2:
					return False

		a = list(A)
		if len(lst_pos) == 2:
			a[lst_pos[0]], a[lst_pos[1]] = a[lst_pos[1]], a[lst_pos[0]]

			if ''.join(a) == B:
				return True
			else:
				return False
		

if __name__ == '__main__':
	sol = Solution()
	print sol.buddyStrings('abab', 'abab')
