#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def dfs(self, node, val):
		if node != None:
			val *= 10
			val += node.val

			if node.left == None and node.right == None:
				return val

			lnum = self.dfs(node.left, val)
			rnum = self.dfs(node.right, val)

			return lnum + rnum
		else:
			return 0

	def sumNumbers(self, root):
		return self.dfs(root, 0)

if __name__ == '__main__':
	root = TreeNode(0)
	root.left = TreeNode(1)
#	root.right = TreeNode(3)

	sol = Solution()
	print(sol.sumNumbers(root))
