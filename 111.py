#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def minDepth(self, root):
		if root == None:
			return 0

		left = self.minDepth(root.left)
		right = self.minDepth(root.right)

		if left == 0 and right == 0:
			return 1
		elif left == 0:
			return 1 + right
		elif right == 0:
			return 1 + left
		else:
			return 1 + min(left, right)


if __name__ == '__main__':
	tnode = TreeNode(3)
	tnode.left = TreeNode(9)
	tnode.right = TreeNode(20)
	tnode.right.left = TreeNode(15)
	tnode.right.right = TreeNode(7)

	sol = Solution()
	print sol.minDepth(tnode)
