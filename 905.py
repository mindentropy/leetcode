#!/usr/bin/env python

#class Solution(object):
#
#	def sortArrayByParity(self, A):
#
#		rtype = [None] * len(A)
#
#		i = 0
#		j = len(A) - 1
#		for val in A:
#			if val & 1:
#				rtype[j] = val
#				j -= 1
#			else:
#				rtype[i] = val
#				i += 1
#
#		return rtype
	
#class Solution(object):
#	def sortArrayByParity(self, A):
#		i = j = 0
#
#		flag = False
#
#		while i < len(A):
#			while j < len(A):
#				if A[j] & 1 == 1 and not flag:
#					flag = True
#					break
#				elif flag == True:
#					break
#
#				j = j + 1
#
#			if A[i] & 1 == 0:
#				if i > j:
#					A[i], A[j] = A[j], A[i]
#					flag = False
#
#			i += 1
#			
#		return A

class Solution(object):
	def sortArrayByParity(self, A):
		i = 0
		j = len(A) - 1

		while i < j:
			if A[i] & 1 == 0 and A[j] & 1 == 1:
				i += 1
				j -= 1
			elif A[i] & 1 == 1 and A[j] & 1 == 0:
				A[i], A[j] = A[j], A[i]
				i += 1
				j -= 1
			elif A[i] & 1 == 0 and A[j] & 1 == 0:
				i += 1
			elif A[i] & 1 == 1 and A[j] & 1 == 1:
				j -= 1
			
		return A

if __name__ == '__main__':
	sol = Solution()
	print sol.sortArrayByParity([1, 3, 5, 7, 10])
