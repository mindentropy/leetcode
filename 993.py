#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isCousins(self, root, x, y):

		lst = []
		parent_nodes = []
		lst.append(root)
		parent = [None]
		prevnode = None

		while(len(lst) != 0):
			valparentmap = {x: None, y: None}

			lvl_lst = []
			while(len(lst) != 0): ## Lvl trav
				node = lst.pop(0)
				parentnode = parent.pop(0)

				if node.val == x or node.val == y:
					valparentmap[node.val] = parentnode
					
				if node.left != None:
					parent.append(node)
					lvl_lst.append(node.left)
				
				if node.right != None:
					parent.append(node)
					lvl_lst.append(node.right)
			
			if valparentmap[x] != valparentmap[y] and valparentmap[x] != None and valparentmap[y]!= None:
				return True

			if lvl_lst != []:
				lst.extend(lvl_lst)

		return False

if __name__ == '__main__':
	
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.right.right = TreeNode(5)

	sol = Solution()
	print(sol.isCousins(root, 5, 4))
