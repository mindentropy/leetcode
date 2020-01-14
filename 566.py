#!/usr/bin/env python

class Solution(object):
	def matrixReshape(self, nums, r, c):
		op = [0] * r
		
		for idx in xrange(r):
			op[idx] = [0] * c
		
		tridx = 0
		tcidx = 0

		for rowidx in xrange(len(nums)):
			for colidx in xrange(len(nums[0])):
				op[tridx][tcidx] = nums[rowidx][colidx]
				tcidx += 1

				if tcidx == c:
					tridx += 1
					tcidx = 0


		if tridx != r or tcidx != 0:
			return nums

		return op
		
if __name__ == '__main__':
	sol = Solution()
	print sol.matrixReshape([[1, 2, 3, 4]], 2, 2)
