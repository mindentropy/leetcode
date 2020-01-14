#!/usr/bin/env python

class Solution(object):
	def distributeCandies(self, candies, num_people):
		op = [0] * num_people
		idx = 0
		candy = 1 

		while True:
			if candies - (candy) <= 0:
				op[idx] += candies
				break
			
			op[idx] += (candy)
			candies -= (candy)

			idx = (idx + 1) % num_people
			candy += 1

		return op

if __name__ == '__main__':
	sol = Solution()
	print sol.distributeCandies(10, 3)
