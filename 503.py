#!/usr/bin/env python

class Solution1(object):
	def nextGreaterElements(self, nums):
		numslen = len(nums)
		result = [-1] * numslen
		
		for idx in range(numslen):

			idx2 = (idx + 1) % numslen
			while idx2 != idx:
				if nums[idx] < nums[idx2]:
					result[idx] = nums[idx2]
					break

				idx2 = (idx2 + 1) % numslen

		return result

class Solution(object):
	def nextGreaterElements(self, nums):
		numslen = len(nums)
		result = [-1] * numslen
		stk = []
		nummap = dict()

		for idx1 in range(numslen):
			idx2 = (idx1 + 1) % numslen 
			while len(stk) != 0 and nums[stk[-1]] < nums[idx1] and idx2 != idx1:
				nummap[stk.pop()] = idx1
				idx2 = (idx2 + 1) % numslen

			stk.append(idx1)

		for idx1 in range(numslen):
			idx2 = (idx1 + 1) % numslen 
			while len(stk) != 0 and nums[stk[-1]] < nums[idx1] and idx2 != idx1:
				nummap[stk.pop()] = idx1
				idx2 = (idx2 + 1) % numslen

		for idx in range(numslen):
			if idx in nummap:
				result[idx] = nums[nummap[idx]]

		return result

if __name__ == '__main__':
	
	a = [1, 2, 1]
	sol = Solution()

	print sol.nextGreaterElements(a)
