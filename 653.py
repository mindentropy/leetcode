#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.inorder_lst = []

#	def inorder(self, root):
#		if root:
#			self.inorder(root.left)
#			self.inorder_lst.append(root.val)
#			self.inorder(root.right)
	
#	def bfs(self, root):
#		node_lst = []	
#
#		node_lst.append(root)
#
#		while len(node_lst):
#			node = node_lst.pop(0)
#
#			self.inorder_lst.append(node.val)
#
#			if node.left != None:
#				node_lst.append(node.left)
#
#			if node.right != None:
#				node_lst.append(node.right)
		
#	def findTarget1(self, root, k):
#		self.inorder(root)
#		
#		idx1 = 0
#		idx2 = len(self.inorder_lst) - 1
#
#		while idx1 < idx2:
#			if self.inorder_lst[idx1] + self.inorder_lst[idx2] < k:
#				idx1 += 1
#			elif self.inorder_lst[idx1] + self.inorder_lst[idx2] > k:
#				idx2 -= 1
#			elif self.inorder_lst[idx1] + self.inorder_lst[idx2] == k:
#			 	return True
				
	
#	def findTarget1(self, root, k):
#		self.bfs(root)
#
#		idx1 = 0
#
#		while idx1 < len(self.inorder_lst):
#			idx2 = idx1 + 1
#			while idx2 < len(self.inorder_lst):
#				if self.inorder_lst[idx1] + self.inorder_lst[idx2] == k:
#					return True
#				idx2 += 1
#			idx1 += 1
#
#		return False


	def find(self, root, k, node_set):
		if root == None:
			return False
		else:
			if (k - root.val) in node_set:
				return True
			else:
				node_set.add(root.val)

				return self.find(root.left, k, node_set) or self.find(root.right, k, node_set)
		
	def findTarget(self, root, k):
		node_set = set()
		return self.find(root, k, node_set) 

if __name__ == '__main__':
	node = TreeNode(5)
	node.left = TreeNode(3)
	node.right = TreeNode(6)

	node.left.left = TreeNode(2)
	node.left.right = TreeNode(4)

	node.right.right = TreeNode(7)

	sol = Solution()
	print sol.findTarget(node, 9)
