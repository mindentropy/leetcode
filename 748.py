#!/usr/bin/env python

class Solution(object):
	def shortestCompletingWord(self, licensePlate, words):
		lp_dict = dict()
		min_word_len = 10000
		min_word = ''
		lp_word_cnt = 0

		for ch in licensePlate.lower():
			if (ord(ch) >= 97 and ord(ch) <= 122):
				lp_dict[ch.lower()] = lp_dict.get(ch, 0) + 1
				lp_word_cnt += 1
		
		for word in words:
			lpd = lp_dict.copy()

			for ch in word:
				if ch in lpd:
					lpd[ch] -= 1
			
			addflag = True
			for key in lpd:
				if lpd[key] > 0:
					addflag = False
					break

			if addflag and min_word_len > len(word):
				min_word = word

				if lp_word_cnt == len(word):
					break

				min_word_len = len(word)

		return min_word

if __name__ == '__main__':
	licensePlate = 'GrC8950'
	words = ['according']

	sol = Solution()
	print sol.shortestCompletingWord(licensePlate, words)
