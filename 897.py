#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def __init__(self):
		self.tnode = None
		self.lastnode = None

	def increasingBST1(self, root):
		if root == None:
			return
		else:
			self.increasingBST1(root.left)

			if self.tnode == None:
				self.tnode = TreeNode(root.val)
				self.lastnode = self.tnode
			else:
				self.lastnode.right = TreeNode(root.val)
				self.lastnode = self.lastnode.right

			self.increasingBST1(root.right)
		
	def increasingBST(self, root):
		self.increasingBST1(root)
		return self.tnode

if __name__ == '__main__':

	tnode = TreeNode(5)
	tnode.left = TreeNode(3)
	tnode.right = TreeNode(6)

	tnode.left.left = TreeNode(2)
	tnode.left.right = TreeNode(4)
	tnode.left.left.left = TreeNode(1)

	tnode.right.right= TreeNode(8)
	tnode.right.right.left = TreeNode(7)
	tnode.right.right.right = TreeNode(9)

	sol = Solution()
	print sol.increasingBST(tnode)
