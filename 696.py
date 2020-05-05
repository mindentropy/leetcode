#!/usr/bin/env python

class Solution(object):
	def countBinarySubstrings(self, s):
		strcnt = 0
		
		i = 0
		while i < len(s) - 1:
			j = i + 1
			oppcnt = 1
			
			eqflag = True
			while j < len(s):
				if s[i] == s[j]:
					if eqflag == False:
						break

					oppcnt += 1
				else:
					oppcnt -= 1
					eqflag = False

				j += 1
				if oppcnt <= 0:
					break

			if oppcnt == 0:
				strcnt += 1
			i += 1

		return strcnt

class Solution(object):
	def countBinarySubstrings(self, s):
		group = [1]

		for idx in xrange(1, len(s)):
			if s[idx - 1] != s[idx]:
				group.append(1)
			else:
				group[-1] += 1

		cnt = 0
		for idx in xrange(len(group) - 1):
			cnt += min(group[idx], group[idx + 1])

		return cnt

if __name__ == '__main__':
	sol = Solution()
	print sol.countBinarySubstrings('00110011')
