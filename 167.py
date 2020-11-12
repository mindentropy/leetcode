#!/usr/bin/env python

class Solution(object):

#	def binsearch(self, numbers, lo, hi, searchnum):
#		if lo > hi:
#			return -1
#		else:
#			mid = (lo + hi)//2
#
#			if numbers[mid] == searchnum:
#				return mid
#			elif searchnum > numbers[mid]:
#				return self.binsearch(numbers, mid + 1, hi, searchnum)
#			elif searchnum < numbers[mid]:
#				return self.binsearch(numbers, lo, mid - 1, searchnum)

	def twopointer(self, numbers, lo, hi, target):
		total = numbers[lo] + numbers[hi]

		if total == target:
			return [lo + 1, hi + 1]
		elif total > target:
			return self.twopointer(numbers, lo, hi - 1, target)
		elif total < target:
			return self.twopointer(numbers, lo + 1, hi, target)
		
	def twoSum(self, numbers, target):
		return self.twopointer(numbers, 0, len(numbers) - 1, target)
	#	idx1 = 0
	#	idx2 = 0
	#	for idx1 in range(len(numbers) - 1):
	#		searchnum = target - numbers[idx1]
	#		idx2 = self.binsearch(numbers, idx1 + 1, len(numbers) - 1, searchnum)

	#		if idx2 != -1:
	#			return [idx1 + 1, idx2 + 1]


if __name__ == '__main__':
	numbers = [2, 7, 11, 15]
	target = 9
	
	sol = Solution()
	print(sol.twoSum(numbers, target))
