#!/usr/bin/env python


class Solution(object):
	def judgeCircle(self, moves):
		"""
		:type moves: str
		:rtype: bool
		"""
        
		x = 0
		y = 0
		
		for idx in range(len(moves)):
			if moves[idx] == 'U':
				y += 1
			elif moves[idx] == 'D':
				y -= 1
			elif moves[idx] == 'L':
				x -= 1
			elif moves[idx] == 'R':
				x += 1

		if x == 0 and y == 0:
			return True
		else:
			return False


if __name__ == '__main__':
	sol = Solution()

	moves = 'UD'
	print sol.judgeCircle(moves)

