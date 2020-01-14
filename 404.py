#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.left_sum = 0

	def sumOfLeftLeaves1(self, root, isLeft):
		if root == None:
			return 0
		else:
			if root.left == None and root.right == None and isLeft:
				self.left_sum+= root.val
				
			self.sumOfLeftLeaves1(root.left, True)
			self.sumOfLeftLeaves1(root.right, False)

			return self.left_sum
		
	def sumOfLeftLeaves(self, root):
		self.sumOfLeftLeaves1(root, 0)
		return self.left_sum

if __name__ == '__main__':

	node = TreeNode(3)
	node.left = TreeNode(9)

	node.right = TreeNode(20)
	node.right.left = TreeNode(15)
	node.right.right = TreeNode(7)

	sol = Solution()
	print sol.sumOfLeftLeaves(node)
