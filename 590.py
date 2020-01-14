#!/usr/bin/env python

class Node(object):
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children
	
class Solution(object):
	def __init__(self):
		self.list = []

	def postorder(self, root):
		"""
		:type root: Node
		:rtype: List[int]
		"""
		
		if root != None:
			
			if root.children != None:
				for child in root.children:
					self.postorder(child)

			self.list.append(root.val)

		return self.list

if __name__ == '__main__':

	node = Node(1)
	node.children = []
	node.children.append(Node(3))
	node.children.append(Node(2))
	node.children.append(Node(4))

	node.children[0].children = []
	node.children[0].children.append(Node(5))
	node.children[0].children.append(Node(6))
	
	sol = Solution()
	print sol.postorder(node)
