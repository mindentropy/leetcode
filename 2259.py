#!/usr/bin/env python


##TODO: Solution, whenever there is a match with the digit, check the next number
# with the present number. If the number that is getting replaced is with a higher number
# exit immediately else continue and do not replace.
## Final number needs to be checked for match and handled appropriately.
class Solution(object):
	def removeDigit(self, number, digit):
		idx = 0
		largest = -1
		last_idx = 0
		for idx in range(len(number) - 1):
			if number[idx] == digit:
				if number[idx + 1] > number[idx]:
					return number[0:idx] + number[idx + 1:]
				last_idx = idx

		if number[idx + 1] == digit:
			return number[0:-1]
		else:
			return number[0:last_idx] + number[last_idx + 1:]
			

#class Solution(object):
#	def removeDigit(self, number, digit):
#		idx = 0
#		largest = -1
#		for idx in range(len(number)):
#			if number[idx] == digit:
#				val = int(number[0:idx] + number[idx + 1:])
#				if val > largest:
#				 	largest = val
#
#		return str(largest)

if __name__ == '__main__':
	number = "551"
	digit = "5"

	sol = Solution()
	print(sol.removeDigit(number, digit))
