#!/usr/bin/env python

class Solution(object):
	def __init__(self):
		self.perm_list = []

	def gen_permute(self, i, available, sol, nums):
		if i == len(nums):
			self.perm_list.append(list(sol))
		else:
			for k in range(len(nums)):
				if available[k]:
					available[k] = False
					sol[i] = nums[k]
					self.gen_permute(i + 1, available, sol, nums)
					available[k] = True
	
	def permute(self, nums):
		available = [True] * len(nums)
		sol = [None] * len(nums)

		self.gen_permute(0, available, sol, nums)

		return self.perm_list

if __name__ == '__main__':
	nums = [1, 2, 3]
	sol = Solution()
	print sol.permute(nums)
