#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

#class Solution(object):
#	def __init__(self):
#		self.arr = []
#
#	def postOrder(self, node):
#		if node != None:
#			self.postOrder(node.left)
#			self.postOrder(node.right)
#			self.arr.append(node.val)
#
#	def postorderTraversal(self, root):
#		self.postOrder(root)
#		return self.arr

class Solution(object):
	def postorderTraversal(self, root):
		stk = []
		arr = []
		lastnode = None
		
		while len(stk) != 0 or root != None:
			if root != None:
				stk.append(root)
				root = root.left
			else:
				peeknode = stk[-1]

				## Check if we are transitioning from left.
				if peeknode.right != None and lastnode != peeknode.right:
					root = peeknode.right
				else:
					arr.append(peeknode.val)
					lastnode = stk.pop()

		return arr

if __name__ == '__main__':

	t = TreeNode(1)
	t.left = TreeNode(2)
	t.right = TreeNode(3)
	t.left.left = TreeNode(4)
	t.left.right = TreeNode(5)

	sol = Solution()
	print sol.postorderTraversal(t)
