#!/usr/bin/env python

class Solution(object):
	def commonChars(self, A):
		op = []
		
		cmpword = A[0]
		
		foundflag = None
		for ch in cmpword:
			for cmpstr in A[1:]:
				if ch in cmpstr and ch != '':
					foundflag = True
					continue
				else:
					foundflag = False
					A[0] = A[0].replace(ch, '', 1)
					break

			if foundflag == True:
				op.append(ch)
				for i in range(1, len(A)):
					A[i] = A[i].replace(ch, '', 1)
		

		return op

if __name__ == '__main__':
	sol = Solution()
	print(sol.commonChars([
			'bella',
			'label',
			'roller'
			]))
