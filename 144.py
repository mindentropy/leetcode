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
#	def preorder(self, t):
#		if t != None:
#			self.arr.append(t.val)
#			self.preorderTraversal(t.left)
#			self.preorderTraversal(t.right)
#		
#	def preorderTraversal(self, root):
#		self.preorder(root)
#		return self.arr

class Solution(object):
	
#	def preorderTraversal(self, root):
#		stk = []
#		arr = []
#
#		while len(stk) != 0 or root != None:
#			if root != None:
#				arr.append(root.val)
#				stk.append(root)
#				root = root.left
#			else:
#				root = stk.pop()
#				root = root.right
#
#		return arr
	
	def preorderTraversal(self, root):
		stk = []
		arr = []
		
		if root == None:
			return arr

		stk.append(root)

		while len(stk) != 0:
			root = stk.pop()
			arr.append(root.val)

			if root.right != None:
				stk.append(root.right)

			if root.left != None:
				stk.append(root.left)

		return arr

if __name__ == '__main__':
	t = TreeNode(1)
	t.left = TreeNode(2)
	t.right = TreeNode(3)

	sol = Solution()
	print sol.preorderTraversal(t)
