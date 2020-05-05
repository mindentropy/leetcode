#!/usr/bin/env python

class Solution(object):
	def reorderLogFiles(self, logs):
		dig_log = []
		let_log = []

		for log in logs:
			
			splitstr = log.split(' ', 1)

			if ord(splitstr[1][0]) >= 48 and ord(splitstr[1][0]) <= 57:
				dig_log.append(log)
			else:
				idx = 0
				if len(let_log) == 0:
					let_log.append(log)
				else:
					for word in let_log:
						log_split = word.split(' ', 1)
						if splitstr[1] < log_split[1]:
							break
						elif splitstr[1] == log_split[1]:
							if splitstr[0] < logsplit[0]:
								break

						idx += 1

					let_log.insert(idx, log)

		return let_log + dig_log

if __name__ == '__main__':
	logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
	sol = Solution()
	print sol.reorderLogFiles(logs)
