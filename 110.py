#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None

class Solution(object):

	def dfs(self, node):
		if node != None:
			if node.left == None and node.right == None:
				return True
			elif node.left == None and node.right != None and (node.right.right != None or node.right.left != None):
				return False
			elif node.right == None and node.left != None and (node.left.left != None or node.left.right != None):
				return False

			leftval = self.dfs(node.left)
			rightval = self.dfs(node.right)

			return leftval and rightval
		else:
			return True

	def isBalanced(self, root):
		return self.dfs(root)

if __name__ == '__main__':
#	root = TreeNode(3)
#	root.left = TreeNode(9)
#	root.right = TreeNode(20)
#	root.right.left = TreeNode(15)
#	root.right.right = TreeNode(7)

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(2)
	root.left.right = TreeNode(3)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(4)
	root.left.left.right = TreeNode(4)

#	root = TreeNode(1)
#	root.left = TreeNode(2)
#	root.left.right = TreeNode(3)

	sol = Solution()
	print(sol.isBalanced(root))
