#!/usr/bin/env python

class Node(object):
	def __init__(self, val = None, children = None):
		self.val = val
		self.children = children


class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0

		if root.children == None:
			return 1

		return 1 + max([self.maxDepth(node) for node in root.children] or [0])
			

if __name__ == '__main__':

	root = Node(1)
	node3 = Node(3)
	node3.children = [None, Node(5), Node(6)]
	root.children =  [None, node3, Node(2), Node(4)]

	sol = Solution()
	print sol.maxDepth(root)
