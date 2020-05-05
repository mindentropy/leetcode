#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def insertIntoBST(self, root, val):
		tmp = root
		prev = None
		node = TreeNode(val)

		while tmp != None:
			prev = tmp
			if tmp.val > val:
				tmp = tmp.left
			elif tmp.val < val:
				tmp = tmp.right

		if prev == None:
			return node
		elif prev.val > val:
			prev.left = node
		elif prev.val < val:
			prev.right = node
		
		return root

	def dispTree(self, node):
		if node != None:
			print node.val
			self.dispTree(node.left)
			self.dispTree(node.right)

if __name__ == '__main__':
	node = TreeNode(4)
	node.left = TreeNode(2)
	node.left.left = TreeNode(1)
	node.left.right = TreeNode(3)
	node.right = TreeNode(7)

	sol = Solution()

	sol.dispTree(node)
	sol.insertIntoBST(node, 5)
	sol.dispTree(node)

