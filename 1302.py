#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.max_depth_sum = 0

	def get_max_depth(self, root):
		if root == None:
			return 0
		else:
			left = 1 + self.get_max_depth(root.left)
			right = 1 + self.get_max_depth(root.right)

			return max(left, right)

	def get_max_depth_sum(self, root, max_depth):
		if root != None:

			if max_depth == 1:
				self.max_depth_sum += root.val 

			self.get_max_depth_sum(root.left, max_depth - 1)
			self.get_max_depth_sum(root.right, max_depth - 1)

	def deepestLeavesSum(self, root):
		self.get_max_depth_sum(root, self.get_max_depth(root))

		return self.max_depth_sum

if __name__ == '__main__':
	sol = Solution()

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.left.left.left = TreeNode(7)

	root.right.right = TreeNode(6)
	root.right.right.right = TreeNode(8)

	print sol.deepestLeavesSum(root)
