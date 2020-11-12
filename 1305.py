#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def __init__(self):
		self.lst1 = []
		self.lst2 = []
		self.mergelst = []
		self.idx1 = 0
		self.idx = 0
		
	def trav_in(self, root, arr):
		if root != None:
			self.trav_in(root.left, arr)
			arr.append(root.val)
			self.trav_in(root.right, arr)

	def trav_in_merge(self, root, arr):
		if root != None:
			self.trav_in_merge(root.left, arr)

			while self.idx1 < len(arr) and arr[self.idx1] < root.val:
				self.mergelst.append(arr[self.idx1])
				self.idx1 += 1

			self.mergelst.append(root.val)

			self.trav_in_merge(root.right, arr)

	def trav_in_test(self, root):
		if root != None:
			self.trav_in_test(root.left)
			print(root.val)
			self.trav_in_test(root.right)

#	def merge_list(self, arr1, arr2):
#		mergelist = []
#		idx1 = 0
#		idx2 = 0
#
#		while idx1 < len(arr1) and idx2 < len(arr2):
#			if arr1[idx1] < arr2[idx2]:
#				mergelist.append(arr1[idx1])
#				idx1 += 1
#			elif arr2[idx2] < arr1[idx1]:
#				mergelist.append(arr2[idx2])
#				idx2 += 1
#			elif arr1[idx1] == arr2[idx2]:
#				mergelist.append(arr1[idx1])
#				mergelist.append(arr2[idx2])
#				idx1 += 1
#				idx2 += 1
#
#		if idx1 < len(arr1):
#			mergelist.extend(arr1[idx1:])
#		elif idx2 < len(arr2):
#			mergelist.extend(arr2[idx2:])
#			
#		return mergelist
		
	def getAllElements(self, root1, root2):
		self.trav_in(root1, self.lst1)
		self.trav_in_merge(root2, self.lst1)

		if self.idx1 < len(self.lst1):
			self.mergelst.extend(self.lst1[self.idx1:])

		return self.mergelst
		#return self.merge_list(self.lst1, self.lst2)

if __name__ == '__main__':
	sol = Solution()

	root1 = TreeNode(0)
	root1.left = TreeNode(-10)
	root1.right = TreeNode(10)

	root2 = TreeNode(1)
	root2.left = TreeNode(0)
	root2.right = TreeNode(3)

	print(sol.getAllElements(root1, root2))
