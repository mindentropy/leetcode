#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.total = 0

	def convertBST(self, root):
		if root:
			self.convertBST(root.right)
			self.total += root.val
			root.val = self.total
			self.convertBST(root.left)

		return root

	def printInOrder(self, root):
		if root:
			self.printInOrder(root.left)
			print root.val
			self.printInOrder(root.right)

if __name__ == '__main__':

	root = TreeNode(5)
	root.left = TreeNode(2)
	root.right = TreeNode(13)

	sol = Solution()
	sol.printInOrder(sol.convertBST(root))
