#!/usr/bin/env python

class Solution(object):

	def __init__(self):
		self.final_sol = []

	def subsets_gen(self, i, sol, nums):
		
		if i == len(nums): ## Base case
			solution = []
			for j in range(0, len(sol)):
				if sol[j] == 1:
					solution.append(nums[j])

			self.final_sol.append(solution)
		else:
			for k in range(0, 2):
				sol = sol + [k]
				
				solu = self.subsets_gen(i + 1, sol, nums)

				del(sol[-1])
		
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		sol = []
		self.subsets_gen(0, sol, nums)
		return self.final_sol

if __name__ == '__main__':
	nums = [1, 2, 3]

	sol = Solution()

	print sol.subsets(nums)
