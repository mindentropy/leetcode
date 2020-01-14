#!/usr/bin/env python

from __future__ import print_function

class Solution(object):

	morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",\
			"-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",\
			"...-",".--","-..-","-.--","--.."]

	def uniqueMorseRepresentations(self, words):
		morseset = set()

		for word in words:
			morseval = ''
			for ch in word:
				morseval += Solution.morse[ord(ch) - ord('a')]
			
			morseset.add(morseval)

		return len(morseset)
		
if __name__ == '__main__':
	sol = Solution()
	print(sol.uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg']))
