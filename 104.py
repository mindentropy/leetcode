#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0
		else:
			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
	tnode = TreeNode(3)
	tnode.left = TreeNode(9)
	tnode.right = TreeNode(20)
	tnode.right.left = TreeNode(15)
	tnode.right.right = TreeNode(7)

	sol = Solution()
	print sol.maxDepth(tnode)
