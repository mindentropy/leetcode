#!/usr/bin/env python

class Solution(object):
	def subdomainVisits(self, cpdomains):

		domain_count = dict()

		for val in cpdomains:
			tmp = val.split(' ')
			count = int(tmp[0])

			strsplit = tmp[1].split('.')
			
			strsplit.reverse()

			prevstr = ""
			for strval in strsplit:
				if prevstr == "":
					strkey = strval + prevstr
				else:
					strkey = strval + "." + prevstr

				if strkey in domain_count:
					domain_count[strkey] += count
				else:
					domain_count[strkey] = count

				prevstr = strkey

		cplist = []
		for key, val in domain_count.items():
			cplist.append(str(val) + " " + key)

		return cplist
		
if __name__ == '__main__':

	cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

	sol = Solution()
	print sol.subdomainVisits(cpdomains)
