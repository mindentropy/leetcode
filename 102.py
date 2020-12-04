#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	
	def bfs(self, root):
		lst = [root]
		numarr = []

		while len(lst) != 0:
			levelnode = []
			arr = []
			while len(lst) != 0:
				node = lst.pop(0)
				arr.extend([node.val])

				if node.left != None:
					levelnode.append(node.left)

				if node.right != None:
					levelnode.append(node.right)
			
			numarr.append(arr)
			lst.extend(levelnode)

		return numarr

	def levelOrder(self, root):
		if root == None:
			return []
		return self.bfs(root)

if __name__ == '__main__':
	sol = Solution()
	
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)

	print(sol.levelOrder(root))
