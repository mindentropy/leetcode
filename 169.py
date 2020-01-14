#!/usr/bin/env python

class Solution(object):
	
	def occurences_in_list(self, nums, x):
		cnt = 0

		for val in nums:
			if val == x:
				cnt += 1

		return cnt
		
	def majority_element(self, nums):
		n = len(nums)
		if n == 0:
			return (False, None, 0)
		elif n == 1:
			return (True, nums[0], 1)
		else:
			b = nums[0:n//2]
			c = nums[n//2:n]

			t = self.majority_element(b)
			if t[0]:
				occurences = self.occurences_in_list(c, t[1])
				if t[2] + occurences > n/2:
					return (True, t[1], t[2] + occurences)

			t = self.majority_element(c)
			if t[0]:
				occurences = self.occurences_in_list(b, t[1])
				if t[2] + occurences > n/2:
					return (True, t[1], t[2] + occurences)

			return (False, None, 0)

	def majorityElement(self, nums):
		return self.majority_element(nums)[1]

if __name__ == '__main__':
	a = [2,2,1,1,1,2,2]
	sol = Solution()

	print sol.majorityElement(a)
