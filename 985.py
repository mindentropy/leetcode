#!/usr/bin/env python

class Solution(object):
	def sumEvenAfterQueries(self, A, queries):
		op = []

		total_even_cnt = 0

		for val in A:
			if val & 1 == 0:
				total_even_cnt += val

		for query in queries:
			prev = A[query[1]]
			A[query[1]] += query[0]
			
			if A[query[1]] & 1 == 0:
				if prev & 1 == 0:
					total_even_cnt += (-prev + A[query[1]])
				else:
					total_even_cnt += A[query[1]]
					
			else:
				if prev & 1 == 0:
					total_even_cnt -= prev
			
			
			op.append(total_even_cnt)

		return op

if __name__ == '__main__':
	A = [1, 2, 3, 4]
	queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
	sol = Solution()
	print sol.sumEvenAfterQueries(A, queries)
