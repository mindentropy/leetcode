import math
class Solution(object):
	
	def f(self, x, num) -> int:
		return x**2 - num

	def bisection(self, a, b, num, epsilon):
		z = (a + b) / 2
		
		if self.f(z, num) == 0 or (b - a) <= (2 * epsilon):
			return z
		elif (self.f(a, num) > 0 and self.f(z, num) < 0) or (self.f(a, num) < 0 and self.f(z, num) > 0):
			return self.bisection(a, z, num, epsilon)
		else:
			return self.bisection(z, b, num, epsilon)

	def mySqrt(self, x):
		if x == 1:
			return 1
		val = self.bisection(0, x, x, 10**-10)
		print(val)
		return math.floor(val)

if __name__ == '__main__':
	sol = Solution()
	print(sol.mySqrt(36))
