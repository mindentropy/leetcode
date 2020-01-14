#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
#	def searchBST(self, root, val):
#		while root != None:
#			if val > root.val:
#				root = root.right
#			elif val < root.val:
#				root = root.left
#			elif val == root.val:
#				return root
#
#		return None
	
	def searchBST(self, root, val):
		if root == None:
			return None
		elif root.val == val:
			return root
		elif val > root.val:
			return self.searchBST(root.right, val)
		elif val < root.val:
			return self.searchBST(root.left, val)

if __name__ == '__main__':
	t = TreeNode(4)
	t.right = TreeNode(7)
	t.left = TreeNode(2)

	t.left.left = TreeNode(1)
	t.left.right = TreeNode(3)

	sol = Solution()
	print(sol.searchBST(t, 3))
