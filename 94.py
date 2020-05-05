#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

#class Solution(object):
#	def __init__(self):
#		self.arr = []
#
#	def inorder(self, t):
#		if t != None:
#			self.inorderTraversal(t.left)
#			self.arr.append(t.val)
#			self.inorderTraversal(t.right)
#		
#	def inorderTraversal(self, root):
#		self.inorder(root)
#		return self.arr

class Solution(object):
	def inorderTraversal(self, root):

		arr = []
		stk = []

		while len(stk) != 0 or root != None:
			if root != None:
				stk.append(root)
				root = root.left
			else:
				root = stk.pop()
				arr.append(root.val)
				root = root.right

		return arr

if __name__ == '__main__':
	t = TreeNode(1)
	t.right = TreeNode(2)
	t.right.left = TreeNode(3)
	
	sol = Solution()
	print sol.inorderTraversal(t)
