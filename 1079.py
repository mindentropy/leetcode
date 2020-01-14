#!/usr/bin/env python

class Solution(object):
	def __init__(self):
		self.perm_set = set()
		self.tile_perm = []
		self.subset = set()

	def gen_subsets(self, sol, tiles):
		if len(sol) == len(tiles):
			string = ''
			for idx in range(len(sol)):
				if sol[idx] == 1:
					string += tiles[idx]

			if not string == '':
				self.perm_set.add(string)
			
		else:
			for k in range(0, 2):
				sol = sol + [k]
				self.gen_subsets(sol, tiles)

				del sol[-1]

	def gen_subset_perm(self, i, available, sol, tileset):
		if i == len(tileset):
			self.subset.add(''.join(sol))
		else:
			for k in range(len(tileset)):
				if available[k]:
					sol[i] = tileset[k]
					available[k] = False
					self.gen_subset_perm(i + 1, available, sol, tileset)

					available[k] = True

	def numTilePossibilities(self, tiles):
		sol = []
		
		self.gen_subsets(sol, tiles)

		for string in self.perm_set:
			available = [True] * len(string)
			sol = [None] * len(string)
			self.gen_subset_perm(0, available, sol, string)

		return len(self.subset)

if __name__ == '__main__':
	tiles = 'AAB'
	
	sol = Solution()
	print sol.numTilePossibilities(tiles)

