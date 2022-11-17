#!/usr/bin/env python

class Solution(object):
	def addBinary(self, a: str, b: str) -> str:
		slen = len(a)
		carry = 0

		i = 0
		final_sum = ''
		while i < slen:
			if len(a) < i or len(b) < i:
				break
			
			if a[slen - i - 1] == '1' and b[slen - i - 1] == '1' and carry == '1':
				final_sum = '1' + final_sum
			elif a[slen - i - 1] == '0':
				if b[slen - i - 1] == '1':
					if carry == '1':
						final_sum = '0' + final_sum
						carry = '1'
					elif carry == 0:
						final_sum = '1' + final_sum
						carry = '0'
			elif b[slen - i - 1] == '0':
				if a[slen - i - 1] == '1':
					if carry == '1':
						final_sum = '0' + final_sum
						carry = '1'
					elif carry == 0:
						final_sum = '1' + final_sum
						carry = '0'
			i += 1

		if i < len(a):
			while i < len(a):
				if carry == '1':
					if a[slen - i - 1] == '1':
						final_sum = '0' + final_sum
					elif a[slen - i - 1] == '0':
						final_sum = carry + final_sum
						carry = 0
				i += 1
		elif i < len(b):
			while i < len(b):
				if carry == '1':
					if b[slen - i - 1] == '1':
						final_sum = '0' + final_sum
					elif b[slen - i - 1] == '0':
						final_sum = carry + final_sum
						carry = 0
				i += 1

		if carry == '1':
			final_sum = carry + final_sum

		return final_sum
				

if __name__ == '__main__':
	a = '11'
	b = '1'

	sol = Solution()
	sol.addBinary(a, b)
