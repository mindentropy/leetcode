#!/usr/bin/env python


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def trav(self, root, tree_leaves):
		if root:
			self.trav(root.left, tree_leaves)
			if root.left == None and root.right == None:
				tree_leaves.append(root.val)
			self.trav(root.right, tree_leaves)
	
	def leafSimilar(self, root1, root2):
		tree1_leaves = []
		tree2_leaves = []
		self.trav(root1, tree1_leaves)
		self.trav(root2, tree2_leaves)

		if len(tree1_leaves) != len(tree2_leaves):
			return False

		idx = 0
		for idx in range(len(tree1_leaves)):
			if tree1_leaves[idx] != tree2_leaves[idx]:
				return False

		return True

if __name__ == '__main__':
	
	node = TreeNode(3)
	node.left = TreeNode(5)
	node.left.left = TreeNode(6)
	node.left.right = TreeNode(2)
	node.left.right.left = TreeNode(7)
	node.left.right.right = TreeNode(4)

	node.right = TreeNode(1)
	node.right.left = TreeNode(9)
	node.right.right = TreeNode(8)


	sol = Solution()
	print sol.leafSimilar(node, node)
