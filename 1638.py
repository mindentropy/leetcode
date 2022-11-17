class Solution(object):
	
	def diffcnt(self, s: str, t: str, sub_len:int):
		i = 0
		diffcnt = 0

		while i < sub_len:
			if s[i] != t[i]:
				diffcnt += 1

			i += 1

		return diffcnt
			
	def countSubstrings(self, s: str, t: str):
		cnt = 0

		for sub_len in range(len(s)):
			for i in range(len(s) - sub_len):
				for j in range(len(t) - sub_len):
					if self.diffcnt(s[i:], t[j:], sub_len + 1) == 1:
						cnt += 1

		print(cnt)
		return cnt

if __name__ == '__main__':
	s = 'aba'
	t = 'baba'

	sol = Solution()
	sol.countSubstrings(s, t)
