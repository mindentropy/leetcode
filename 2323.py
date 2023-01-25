#!/usr/bin/env python
import math

class Solution(object):
	def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
		jobs.sort(reverse=True)
		workers.sort(reverse=True)

		op = 0

## Disregard the example. You assign longest job to the hardest worker.
## Take the ratio and then check the max.
		for idx in range(len(jobs)):
			#print(jobs[idx] // workers[idx])
			val = math.ceil(jobs[idx] / workers[idx])
			op = max(op, math.ceil(jobs[idx]/workers[idx]))

		return op


if __name__ == '__main__':
#	jobs = [5, 2, 4]
#	workers = [1, 7, 5]

	jobs = [1]
	workers = [2]

	sol = Solution()
	print(sol.minimumTime(jobs, workers))
