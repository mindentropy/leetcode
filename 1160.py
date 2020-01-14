#!/usr/bin/env python

class Solution(object):
	def countCharacters(self, words, chars):

		final_word = ""
		char_hash = {}

		for char in chars:
			if char not in char_hash:
				char_hash[char] = 0
			else:
				char_hash[char] += 1

		
		for word in words:
			found = True
			hash_cmp = char_hash.copy()
			for ch in word:
				if ch in hash_cmp:
					if hash_cmp[ch] < 0:
						found = False
						break
					hash_cmp[ch] -= 1
				else:
					found = False
					break

			if found == True:
				final_word += word

		return len(final_word)

if __name__ == '__main__':
	sol = Solution()

	words = ['cat', 'bt', 'hat', 'tree']
	chars = 'atach'

	print sol.countCharacters(words, chars)
