#!/usr/bin/env python

class Node(object):
	def __init__(self, val = None, children = None):
		self.val = val
		self.children = children

class Solution(object):
	def __init__(self):
		self.lvllst = []

	def bfs(self, nodelst):
		cnodearr = []
		arr = []
		
		if len(nodelst) == 0:
			return

		while len(nodelst) != 0:
			node = nodelst.pop(0)
			arr.append(node.val)

			if node.children != None:
				for nodes in node.children:
					cnodearr.append(nodes)
		
		self.lvllst.append(arr)
		self.bfs(cnodearr)

	def levelOrder(self, root):
		if root == None:
			return []
		self.bfs([root])
		return self.lvllst

if __name__ == '__main__':
	root = Node(1)
	root.children = [ Node(3), Node(2), Node(4) ]
	root.children[0].children =  [ Node(5), Node(6) ]

	sol = Solution()
	print(sol.levelOrder(root))
