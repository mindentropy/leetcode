#!/usr/bin/env python

class Solution(object):
	def tictactoe(self, moves):
		board = [[None] * 3, [None] * 3, [None] * 3]

		ch = 'X'
		for val in moves:
			board[val[0]][val[1]] = ch

			if ch == 'X':
				ch = 'O'
			else:
				ch = 'X'

		print board

		for rows in xrange(3):
			xcount1 = 0
			ocount1 = 0
			
			xcount2 = 0
			ocount2 = 0

			for cols in xrange(3):
				if board[rows][cols] == 'X':
					xcount1 += 1
				elif board[rows][cols] == 'O':
					ocount1 += 1

				if board[cols][rows] == 'X':
					xcount2 += 1
				elif board[cols][rows] == 'O':
					ocount2 += 1

				if xcount1 == 3 or xcount2 == 3:
					return 'A'
				elif ocount1 == 3 or ocount2 == 3:
					return 'B'

		if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
			return 'A'
		elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
			return 'B'
		elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
			return 'B'
		elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
			return 'A'

		if len(moves) == 9:
			return 'Draw'
		else:
			return 'Pending'

if __name__ == '__main__':

	moves =  [[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]]

	sol = Solution()
	print sol.tictactoe(moves)
