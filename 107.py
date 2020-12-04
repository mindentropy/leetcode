#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def bfs(self, root):
		lst = []
		bott_up_nodes = []

		if root == None:
			return bott_up_nodes

		lst.append(root)

		while len(lst) != 0:
			nodeval = []
			lvlnode = []
			while len(lst) != 0:
				node = lst.pop(0)
				nodeval += [node.val]
				
				if node.left != None:
					lvlnode.append(node.left)

				if node.right != None:
					lvlnode.append(node.right)

			bott_up_nodes = [nodeval] + bott_up_nodes

			if lvlnode != []:
				lst.extend(lvlnode)

		return bott_up_nodes
		
	def levelOrderBottom(self, root):
		return self.bfs(root)

if __name__ == '__main__':

	#root = TreeNode(3)
	#root.left = TreeNode(9)
	#root.right = TreeNode(20)

	#root.right.left = TreeNode(15)
	#root.right.right = TreeNode(7)

	root = TreeNode(1)

	root.left = TreeNode(2)
	root.right = TreeNode(3)

	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)

	sol = Solution()
	print(sol.levelOrderBottom(root))
