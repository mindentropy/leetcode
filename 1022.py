#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.final_total = 0

	def rootToLeaf(self, root, total):
		if root:
			total = total<<1 | root.val
			
			if root.left == None and root.right == None:
				self.final_total += total

			self.rootToLeaf(root.left, total)
			self.rootToLeaf(root.right, total)

	def sumRootToLeaf(self, root):
		self.rootToLeaf(root, 0)
		return self.final_total

if __name__ == '__main__':
	node = TreeNode(1)

	node.left = TreeNode(0)
	node.left.left = TreeNode(0)
	node.left.right = TreeNode(1)

	node.right = TreeNode(1)
	node.right.left = TreeNode(0)
	node.right.right = TreeNode(1)

	sol = Solution()
	print sol.sumRootToLeaf(node)
