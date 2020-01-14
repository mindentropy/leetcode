#!/usr/bin/env python

class Solution(object):
	def numRookCaptures(self, board):
		
		rook_pos = []

		for row in range(8):
			for col in range(8):
				if board[row][col] == 'R':
					rook_pos.append((row, col))
					break

		## Step in 4 cardinal directions 
		row = rook_pos[0][0] - 1
		col = rook_pos[0][1]

		capcount = 0

		## North
		while row >= 0:
			if board[row][col] == 'B':
				break
			elif board[row][col] == 'p':
				capcount += 1
				break

			row -= 1


		row = rook_pos[0][0] + 1
		col = rook_pos[0][1]
		## South
		while row < 8:
			if board[row][col] == 'B':
				break
			elif board[row][col] == 'p':
				capcount += 1
				break

			row += 1

		row = rook_pos[0][0]
		col = rook_pos[0][1] + 1

		## East
		while col < 8:
			if board[row][col] == 'B':
				break
			elif board[row][col] == 'p':
				capcount += 1
				break

			col += 1

		row = rook_pos[0][0]
		col = rook_pos[0][1] - 1
		## West
		while col >= 0:
			if board[row][col] == 'B':
				break
			elif board[row][col] == 'p':
				capcount += 1
				break

			col -= 1

		return capcount

if __name__ == '__main__':
	sol = Solution()

	board =    [[".",".",".",".",".",".",".","."],
				[".",".",".","p",".",".",".","."],
				[".",".",".","R",".",".",".","p"],
				[".",".",".",".",".",".",".","."],
				[".",".",".",".",".",".",".","."],
				[".",".",".","p",".",".",".","."],
				[".",".",".",".",".",".",".","."],
				[".",".",".",".",".",".",".","."]]
	
	print sol.numRookCaptures(board)
