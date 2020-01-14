#!/usr/bin/env python

from collections import deque

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None


class Solution(object):
	def isUnivalTree(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		que = deque()
		que.appendleft(root)
		
		val = root.val

		while len(que) != 0:
			node = que.pop()

			if val != node.val:
				return False

			if node.left != None:
				que.appendleft(node.left)

			if node.right != None:
				que.appendleft(node.right)
		
		return True

if __name__ == '__main__':

	node = TreeNode(1)
	node.left = TreeNode(1)
	node.right = TreeNode(1)

	node.left.left = TreeNode(1)
	node.left.right = TreeNode(1)

	node.right.right = TreeNode(1)

	sol = Solution()

	print sol.isUnivalTree(node)
