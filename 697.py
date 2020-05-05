#!/usr/bin/env python

class Solution(object):
	def findShortestSubArray(self, nums):
		
		freq = dict()
		maxfreq = -1

		for val in nums:
			freq[val] = freq.get(val, 0) + 1

			if freq[val] > maxfreq:
				maxfreq = freq[val]

		deg = 1000000
		for val in freq:
			if freq[val] == maxfreq:

				left = 0
				while left < len(nums):
					if nums[left] == val:
						break
					
					left += 1

				right = len(nums) - 1
				while right > 0:
					if nums[right] == val:
						break

					right -= 1
				
				lst_cnt = right - left + 1
				if deg > lst_cnt:
					deg = lst_cnt
					
	#			cnt = maxfreq

	#			idx = 0
	#			for idx in range(len(nums)):
	#				if nums[idx] == val:
	#					cnt -= 1
	#					break

	#			lst_cnt = 1
	#			idx += 1

	#			while idx < len(nums) and cnt > 0:
	#				if nums[idx] == val:
	#					cnt -= 1

	#				idx += 1
	#				lst_cnt += 1

	#			if lst_cnt < deg:
	#				deg = lst_cnt
					
		return deg
		
if __name__ == '__main__':
	sol = Solution()
	print sol.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
