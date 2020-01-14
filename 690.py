#!/usr/bin/env python

class Employee(object):
	def __init__(self, id, importance, subordinates):
		
		self.id = id
		self.importance = importance
		self.subordinates = subordinates

class Solution(object):
	
	def get_emp(self, employees, id):
		for emp in employees:
			if id == emp.id:
				return emp
		
	def getImportance(self, employees, id):
		idlist = []

		imp = 0
		emp = self.get_emp(employees, id)

		imp += emp.importance
		idlist.extend(emp.subordinates)

		while len(idlist) != 0:
			emp = self.get_emp(employees, idlist.pop(0))
			imp += emp.importance
			idlist.extend(emp.subordinates)
			
		return imp

if __name__ == '__main__':
	arr = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
	sol = Solution()
	print sol.getImportance(arr, 1)
