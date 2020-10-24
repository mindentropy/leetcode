#!/usr/bin/env python

class Solution(object):
	
	def bin_search_wrap(self, letters, target, lo, hi):
		if lo > hi:
			return letters[lo % len(letters)]
		else:
			mid = (lo + hi)//2

			if letters[mid] == target:
				idx = mid
				while idx <= hi:
					if letters[idx] != target:
						return letters[idx]
					idx += 1

				return letters[(hi + 1) % len(letters)]

			elif ord(letters[mid]) < ord(target):
				return self.bin_search_wrap(letters, target, mid + 1, hi)
			else:
				return self.bin_search_wrap(letters, target, lo, mid - 1) 
	
	def nextGreatestLetter(self, letters, target):
		return self.bin_search_wrap(letters, target, 0, len(letters) - 1)
		
if __name__ == '__main__':
	sol = Solution()

#	letters = ['c', 'f', 'j']
#	target = 'a'

	letters =  ["e","e","e","e","e","e","n","n","n","n"]
	target = 'e'

	print(sol.nextGreatestLetter(letters, target))
