#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def inorder(self, root):
		if root:
			print root.val
			self.inorder(root.left)
			self.inorder(root.right)

	def conv_arr_to_bst(self, nums, start, end):
		if start > end:
			return None
		
		middle = start + (end - start)/2
		node = TreeNode(nums[middle])

		node.left = self.conv_arr_to_bst(nums, start, middle - 1)
		node.right = self.conv_arr_to_bst(nums, middle + 1 , end)

		return node

	def sortedArrayToBST(self, nums):
		if len(nums) == 0:
			return None
		
		return self.conv_arr_to_bst(nums, 0, len(nums) - 1)


if __name__ == '__main__':
	nums = [1, 3]

	sol = Solution()
	root = None
#	root = sol.add_node(root, 2)
#	root = sol.add_node(root, 1)
#	root = sol.add_node(root, 0)
#	root = sol.add_node(root, 5)
#	root = sol.add_node(root, 4)
#	root = sol.add_node(root, 3)

#	sol.inorder(root)
	sol.inorder(sol.sortedArrayToBST(nums))
