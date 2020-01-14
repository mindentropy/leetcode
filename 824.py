#!/usr/bin/env python

class Solution(object):
	def toGoatLatin(self, S):
		op = ''
		wordlist = S.split()

		idx = 1
		for word in wordlist:
			if word[0].lower() == 'a' or word[0].lower() == 'e' or word[0].lower() == 'i' or \
						word[0].lower() == 'o' or word[0].lower() == 'u':
				word += 'ma'
			else:
				word = word[1:] + word[0] + 'ma'
			
			word += 'a' * idx
			idx += 1
			op += word + ' '

		op = op[0:len(op) - 1]
		return op
		
if __name__ == '__main__':
	sol = Solution()
	print sol.toGoatLatin('over')
