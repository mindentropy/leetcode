#!/usr/bin/env python

class Solution(object):
	def canWinNim(self, n):
		
		if n % 4 == 0:
			return False
		else:
			return True

		turn = 0

		if n < 4:
			return True

		while True:
			if n == 4:
				break
			elif (n - 1 == 4) or (n - 2 == 4) or (n - 3 == 4):
				turn = (turn + 1) % 2
				break
			
			if n - 3 > 4 and (n - 2 != 4 or n - 1 != 4):
				n = n - 3
			elif n - 2 > 4 and (n - 1 != 4 or n - 3 != 4):
				n = n - 2
			elif n - 1 > 4 and (n - 2 != 4 or n - 3 != 4):
				n = n - 1
			
			turn = (turn + 1) % 2

		if turn == 0:
			return False
		else:
			return True

if __name__ == '__main__':
	sol = Solution()
	print sol.canWinNim(10)
