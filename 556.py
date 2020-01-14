#!/usr/bin/env python

class Solution(object):
	def nextGreaterElement(self, n):
		val = n

		stk = []
		dec = 1

		num = 0
		while val:
			num = val % 10
			if len(stk) > 0 and stk[-1] > num:
				val /= 10
				dec *= 10
				break

			val /= 10
			dec = dec * 10
			stk.append(num)
			
		val += stk.pop() * dec
		dec /= 10
		
		val += dec
		dec /= 10

		while len(stk) != 0:
			val += stk.pop() * dec
			dec /= 10

		return val 

if __name__ == '__main__':
	n = 3789
	sol = Solution()
	print sol.nextGreaterElement(n)

