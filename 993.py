#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isCousins(self, root, x, y):
		lst = []
		lvl_lst = []
		lst.append(root)

		while(len(lst) != 0):
			for idx in range(len(lst)): ## Lvl trav
				node = lst.pop(0)

				if node.left != None:
					lst.append(node.left)
					lvl_lst.append([node, node.left.val])
				
				if node.right != None:
					lst.append(node.right)
					lvl_lst.append([node, node.right.val])
			

if __name__ == '__main__':
	
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)

	sol = Solution()
	print sol.isCousins(root, 2, 3)
