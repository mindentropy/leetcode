#!/usr/bin/env python


class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):

		idx = 0
		if 1 in flowerbed:
			found_idx = flowerbed.index(1)
			idx = found_idx - 2
		else:
			found_idx = 0

		while idx >= 0 and n != 0:
			if flowerbed[idx] == 0:
				n -= 1
				flowerbed[idx] = 1

			idx -= 2

		
		idx = found_idx + 2
		while idx < len(flowerbed) and n != 0:
			if flowerbed[idx] == 0:
				if (idx + 1) < len(flowerbed):
					if flowerbed[idx + 1] == 1:
						idx = idx + 1 ## Set the index to the value 1 and
									  ## get incremented by two below.
					else:
						n -= 1
						flowerbed[idx] = 1
				else:
					#We are at the end. Set to 1 and decrement.
					flowerbed[idx] = 1
					n -= 1

			idx += 2

		if n == 0:
			return True
		else:
			return False

if __name__ == '__main__':
	sol = Solution()
	print(sol.canPlaceFlowers([0], 1))

