#!/usr/bin/env python


## TODO: Need to optimize the below steps.
class Solution(object):
	def repeatedStringMatch(self, A, B):

		astr = ''
		cnt = 0

		mult = len(B)/len(A)

		if mult == 0:
			astr += A
			cnt = 1
			i = 0
			while i < 2:
				if B in astr:
					return cnt
				else:
					i += 1
					cnt += 1
					astr += A

			return -1
		
		astr = astr + (A * mult)
		
		cnt += mult
		
		if len(B) % len(A) == 0:
			if B in astr:
				return cnt
			
			astr += A

			if B in astr:
				return cnt + 1
		else:
			i = 0
			astr += A
			cnt += 1
			while i < 2:
				if B in astr:
					return cnt
				else:
					cnt += 1
					i += 1
					astr += A

		return -1

if __name__ == '__main__':
	sol = Solution()

	print (sol.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba"))
