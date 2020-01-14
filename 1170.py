#!/usr/bin/env python

class Solution(object):

	def freq_calc(self, string):
		smallest_char = '{'

		freq = dict()

		for ch in string:
			if ch < smallest_char:
				smallest_char = ch

			freq[ch] = freq.get(ch, 0) + 1

		return freq[smallest_char]
		
	def numSmallerByFrequency(self, queries, words):
		
		answers = [0] * len(queries)
		q_freq = []
		w_freq = []

		for qw in queries:
			q_freq.append(self.freq_calc(qw))

		for w in words:
			w_freq.append(self.freq_calc(w))

		idx = 0
		for qf in q_freq:
			cnt = 0
			for wf in w_freq:
				if qf < wf:
					cnt += 1

			answers[idx] = cnt
			idx += 1

		return answers

if __name__ == '__main__':
	sol = Solution()
	print sol.numSmallerByFrequency(['bbb', 'cc'], ['a', 'aa', 'aaa', 'aaaa'])
