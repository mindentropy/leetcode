#!/usr/bin/env python

class SelectionSort(object):
	def __init__(self):
		pass

	def sort(self, nums):
		
		for i in xrange(len(nums)):
			min_idx = i
			for j in xrange(i + 1, len(nums)):
				if nums[i] > nums[j]:
					min_idx = j

			nums[i], nums[min_idx] = nums[min_idx], nums[i]

		return nums
				

if __name__ == '__main__':
	sel = SelectionSort()
	print sel.sort([5, 4, 3, 2, 1])
