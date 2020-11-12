#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

##TODO: Solve iteratively.

class Solution(object):
	
	def __init__(self):
		self.maxsum = -1000000
		self.level = 0

	def bfs(self, nodearr, maxsum, lvl):

		totalsum = 0
		layernode = []
		
		if len(nodearr) == 0:
			return

		while len(nodearr):
			node = nodearr.pop(0)

			totalsum += node.val
			
			if node.left != None
				layernode.append(node.left)

			if node.right != None:
				layernode.append(node.right)
		
		if totalsum > maxsum:
			maxsum = totalsum
			self.level = lvl

		self.bfs(layernode, maxsum, lvl + 1)

	def maxLevelSum(self, root):
		lvl = 0
		self.bfs([root], -1000000, lvl)
		return self.level + 1

if __name__ == '__main__':
	node = TreeNode(1)
	node.left = TreeNode(7)
	node.right = TreeNode(0)

	node.left.left = TreeNode(7)
	node.left.right = TreeNode(-8)

	sol = Solution()
	print(sol.maxLevelSum(node))
