#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def averageOfLevels(self, root):
		node_lst = []

		avg_list = []


		node_lst.append(root)

		while len(node_lst):
			avg = 0
			idx = 0
			for idx in range(len(node_lst)):
				node = node_lst.pop(0)
				avg += node.val
				if node.left != None:
					node_lst.append(node.left)

				if node.right != None:
					node_lst.append(node.right)
			
			avg_list.append((float(avg)/(idx + 1)))

		return avg_list

if __name__ == '__main__':
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)

	sol = Solution()
	print sol.averageOfLevels(root)
