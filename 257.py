#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def dfs(self, node, nodestr):
		if node != None:
			if node.left == None and node.right == None:
				return [nodestr+str(node.val)]
			
			lstr = self.dfs(node.left, nodestr+str(node.val)+"->")
			rstr = self.dfs(node.right, nodestr+str(node.val)+"->")

			arr = []

			if lstr != []:
				arr.extend(lstr)

			if rstr != []:
				arr.extend(rstr)

			return arr
		else:
			return []
		
	def binaryTreePaths(self, root):
		return self.dfs(root, "")
		
if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.right = TreeNode(5)

	sol = Solution()
	print(sol.binaryTreePaths(root))
