#!/usr/bin/env python


## Can be optimized to use n - 1 rather than n and finally subtracting by -1
class Solution(object):
	def convertToTitle(self, n):
		numlst = []
		while(n):
			num = n % 26
			n = n / 26

			if num == 0:
				numlst.insert(0, 'Z')
				n = n - 1
			else:
				numlst.insert(0, chr(num + 64))

		return ''.join(numlst)

if __name__ == '__main__':
	sol = Solution()
	
	for i in range(1, 53):
		sol.convertToTitle(i)
