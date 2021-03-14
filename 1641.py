#!/usr/bin/env python

class Solution(object):
	def __init__(self):
		self.count = 0

	def count_vowel_strings(self, n:int, gen_lst):
		if n == 0:
			self.count += 1
			#print(gen_lst)
			return
		else:
			if len(gen_lst) > 0:
				k = gen_lst[-1]
			else:
				k = 0

			while k < 5:
				gen_lst += [k]
				self.count_vowel_strings(n - 1, gen_lst)
				k += 1
				del(gen_lst[-1])
		
	def countVowelStrings(self, n: int) -> int:
		gen_lst = []
		self.count_vowel_strings(n, gen_lst)
		return self.count


#	def count_vowel_strings(self, n:int, gen_lst, vow_lst):
#		if n == 0:
#			print(gen_lst)
#			self.count += 1
#			return
#		else:
#			k = 0
#			while k < len(vow_lst):
#				if len(gen_lst) > 0 and ord(gen_lst[-1]) > ord(vow_lst[k]):
#					k += 1
#					continue
#
#				gen_lst += [vow_lst[k]]
#				self.count_vowel_strings(n - 1, gen_lst, vow_lst)
#				k += 1
#				del(gen_lst[-1])
#		
#	def countVowelStrings(self, n: int) -> int:
#		gen_lst = []
#		vow_lst = ['a', 'e', 'i', 'o', 'u']
#		self.count_vowel_strings(n, gen_lst, vow_lst)
#		return self.count

if __name__ == '__main__':
	sol = Solution()

	print(sol.countVowelStrings(3))
