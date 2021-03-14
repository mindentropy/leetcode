#!/usr/bin/env python

class Solution(object):
	def validateIPv4(self, IP: str) -> bool:
		

	def validateIPv6(self, IP: str) -> bool:
		pass

	def validIPAddress(self, IP: str) -> str:
		for ch in IP:
			if ch == '.':
				if self.validateIPv4(IP) == True:
					return "IPv4"
				else
					return "Neither"

			if ch == ':':
				if self.validateIPv6(IP) == True:
					return "IPv6"
				else
					return "Neither"

if __name__ == '__main__':
	ip = '1.1.1.1'
#	ip = '0:0:0:0:0:0:0:0'
	sol = Solution()
	sol.validIPAddress(ip)
