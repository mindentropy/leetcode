#!/usr/bin/env python
from typing import List

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def __init__(self):
		self.sorted_list = []

	def inorder_trav(self, node: TreeNode):
		if node == None:
			return

		self.inorder_trav(node.left)
		self.sorted_list.append(node.val)
		self.inorder_trav(node.right)

	def print_inorder_trav(self, node: TreeNode):
		if node == None:
			return

		self.print_inorder_trav(node.left)
		print(node.val)
		self.print_inorder_trav(node.right)

	def sortedArrayToBST(self, slist: List) -> TreeNode:
		slen = len(slist)
		
		if slen == 1:
			return TreeNode(slist[0])
		elif slen == 0:
			return None

		mid = slen//2
		return TreeNode(
				slist[mid], 
				self.sortedArrayToBST(slist[:mid]),
				self.sortedArrayToBST(slist[mid+1:])
			)

	def balanceBST(self, root: TreeNode) -> TreeNode:
		self.inorder_trav(root)
		return self.sortedArrayToBST(self.sorted_list)
	
if __name__ == '__main__':
	node = TreeNode(1)
	node.right = TreeNode(2)
	node.right.right = TreeNode(3)

	sol = Solution()
	n = sol.balanceBST(node)
	sol.print_inorder_trav(n)
