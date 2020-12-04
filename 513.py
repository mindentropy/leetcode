#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def __init__(self):
		self.lvl = -1
		self.nodeval = 0
	
	## Value is left most node.
	## In case of [1,2,3, null, 6, 5, null] it should be 6
	## since it forms the left most.

	## Hence we have to move from left to right.
	def dfs(self, node, lvl, prevnode):
		#print(node.val)
		if node.left == None and node.right == None:
			if self.lvl < lvl:
				self.nodeval = node.val
				self.lvl = lvl
			
		if node.left != None:
			self.dfs(node.left, lvl + 1, node)
		if node.right != None:
			self.dfs(node.right, lvl + 1, node)

	def findBottomLeftValue(self, root):
		if root.left == None and root.right == None:
			return root.val

		self.dfs(root, 0, None)
		return self.nodeval

if __name__ == '__main__':
	sol = Solution()
	
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.right = TreeNode(6)

	root.right = TreeNode(3)
	root.right.left = TreeNode(5)


#	root = TreeNode(1)
#	root.right = TreeNode(3)
#	root.right.left = TreeNode(4)
#	root.left = TreeNode(2)
#	root.left.left = TreeNode(5)

#	root = TreeNode(1)
#	root.left = TreeNode(2)
#	root.right = TreeNode(3)
#	root.left.left = TreeNode(4)
#
#	root.right.left = TreeNode(5)
#	root.right.left.left = TreeNode(7)
#	root.right.right = TreeNode(6)

	print(sol.findBottomLeftValue(root))
