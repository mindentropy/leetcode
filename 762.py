#!/usr/bin/env python

class Solution(object):
	def countPrimeSetBits(self, L, R):
		primes = {2:0, 3:0, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0}

		while(L <= R):
			num = L
			bitcnt = 0
			while num:
				bitcnt += num & 1
				num >>= 1
			
			if bitcnt in primes:
				primes[bitcnt] += 1

			L += 1

		totalcnt = 0
		for key in primes:
			totalcnt += primes[key]
		
		return totalcnt

if __name__ == '__main__':
	sol = Solution()
	print sol.countPrimeSetBits(6, 10)
