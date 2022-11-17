#!/usr/bin/env python

from typing import List

#class Solution:
#	def numTeams(self, rating: List[int]) -> int:
#		total_teams = 0
#
#		for i in range(len(rating) - 2):
#			j = i + 1
#			while j < len(rating) - 1:
#				k = j + 1
#				while k < len(rating):
#					if rating[i] < rating[j] and rating[j] < rating[k] or \
#							rating[i] > rating[j] and rating[j] > rating[k]:
#						total_teams += 1
#
#					k += 1
#				j += 1
#			i += 1
#
#		return total_teams


#class Solution:
#    def numTeams(self, rating: List[int]) -> int:
#        n = len(rating)
#        dp = [[0 for i in range(3)] for i in range(n)]
#        res = 0
#        
#        for i in range(n):
#            dp[i][0] = 1
#            for j in range(i):
#                if rating[j] < rating[i]:
#                    dp[i][1] += dp[j][0]
#                    res += dp[j][1]
#                if rating[j] > rating[i]:
#                    dp[i][2] += dp[j][0]
#                    res += dp[j][2]
#                print(dp)
#        return res

#class Solution:
#	def numTeams(self, rating: List[int]) -> int:
#		n = len(rating)
#		dp_g = [0] * n
#		dp_l = [0] * n
#		res = 0
#
#		for i, r in enumerate(rating):
#			for j in range(i):
#				if r > rating[j]:
#					dp_g[i] += 1
#					res += dp_g[j]
#				
#				if r < rating[j]:
#					dp_l[i] += 1
#					res += dp_l[j]
#
#		return res

#class Solution:
#	def numTeams(self, rating: List[int]) -> int:
#		n = len(rating)
#		dp_g = [0] * n
#		dp_l = [0] * n
#		res = 0
#
#		## We set the counts of all values which are
#		## greater (or lesser) from the current indexed rating
#		for i in range(len(rating)):
#			for j in range(i + 1, len(rating)):
#				if rating[j] > rating[i]:
#					dp_g[i] += 1
#				elif rating[j] < rating[i]:
#					dp_l[i] += 1
#	
#		## This is crucial step: We compare the first rating in 'i' with 'j' and
#		## we add all the value from the present dp_count which is the range of values
#		## greater than the two values which forms the basis of k.
#		## For eg: in the case of [2, 5, 3, 4, 1] we have dp_g [3, 0, 1, 0, 0]. Here
#		## For value 5 there are no values greater than 5 when we have form the sequence
#		## -> 2, 5 with no third value. 
#		## For the value 3 there is 1 value greater. So the combination of teams
#		## that can be formed is 1. Hence we have the result -> 2, 3, 4
#		## The rating[i] > rating[j] or rating[i] < rating[j] makes sure the first two
#		## values in the tuple are validated.
#		for i in range(len(rating) - 2):
#			for j in range(i + 1, len(rating)):
#				if rating[j] > rating[i]:
#					res += dp_g[j]
#				elif rating[j] < rating[i]:
#					res += dp_l[j]
#
#		return res

class Solution:
	def numTeams(self, rating: List[int]) -> List:
		asc = dsc = 0
		

		## This method is a simple counting problem method. For 'rating[i]<rating[j]<rating[k]' 
		## We find the less than numbers from the left and the greater than number from the right.
		## After this it becomes a simple counting problem of combinations. For every 'm' value in 
		## the left and every value 'n' in the right we can have m*n combinations
		for i in range(len(rating)):
			lgc = llc = rgc = rlc = 0
			for val in rating[:i]:
				if val < rating[i]:
					llc += 1
				elif val > rating[i]:
					lgc += 1

			for val in rating[i+1:]:
				if val < rating[i]:
					rlc += 1
				elif val > rating[i]:
					rgc += 1


			asc += llc * rgc
			dsc += lgc * rlc

		return asc + dsc

if __name__ == '__main__':
	rating = [1, 2, 3, 4]
	sol = Solution()

	print(sol.numTeams(rating))
