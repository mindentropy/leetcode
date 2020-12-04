#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.right = right
		self.left = left

class Solution(object):

	def dfs(self, node, maxnode):
		gn_count = 0
		if node != None:
			if node.val >= maxnode:
				maxnode = node.val
				gn_count += 1

			return gn_count + self.dfs(node.left, maxnode) + self.dfs(node.right, maxnode)

		return 0
		
	def goodNodes(self, root):
		return self.dfs(root, -100000)

if __name__ == '__main__':

	root = TreeNode(3)
	root.left = TreeNode(1)
	root.left.left = TreeNode(3)
	root.right = TreeNode(4)
	root.right.right = TreeNode(5)
	root.right.left = TreeNode(1)
	
	sol = Solution()
	print(sol.goodNodes(root))
