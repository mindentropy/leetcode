#!/usr/bin/env python

class Solution(object):
	def findWords(self, words):
		keyboard_rows = [['qwertyuiop'], ['asdfghjkl'], ['zxcvbnm']]

		ans = []
		for word in words:
			for kb_row_word in keyboard_rows:
				found = True
				for idx in range(len(word)):
					if word[idx].lower() not in kb_row_word[0]:
						found = False
						break
				
				if found:
					ans.append(word)

		return ans


if __name__ == '__main__':
	words = ['a', 'b']
	sol = Solution()
	print sol.findWords(words)
