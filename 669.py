#!/usr/bin/env python

##TODO: Took the solution from discuss. Need to get
## an intuitive feel about this.

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def trim(self, root, L, R):
		if root == None:
			return None
		elif root.val < L:
			return self.trim(root.right, L, R)
		elif root.val > R:
			return self.trim(root.left, L, R)
		else:
			root.left = self.trim(root.left, L, R)
			root.right = self.trim(root.right, L, R)

			return root

	def trimBST(self, root, L, R):
		return self.trim(root, L , R)
	
	def inOrder(self, root):
		if root != None:
			print root.val
			self.inOrder(root.left)
			self.inOrder(root.right)

if __name__ == '__main__':

	node = TreeNode(3)
	node.left = TreeNode(1)
	node.right = TreeNode(4)
	node.left.right = TreeNode(2)

#	node = TreeNode(1)
#	node.left = TreeNode(0)
#	node.right = TreeNode(2)

	sol = Solution()
	sol.inOrder(sol.trimBST(node, 3, 4))
