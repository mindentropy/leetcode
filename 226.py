#!/usr/bin/env python


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def invertTree(self, root):
		if root:
			right = self.invertTree(root.right)
			left = self.invertTree(root.left)
			
			root.left = right
			root.right = left
			
			return root

		else:
			return None
			
if __name__ == '__main__':
	root = TreeNode(4)

	root.left = TreeNode(2)
	root.right = TreeNode(7)

	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)

	root.right.left = TreeNode(6)
	root.right.right = TreeNode(9)

	sol = Solution()
	sol.invertTree(root)
