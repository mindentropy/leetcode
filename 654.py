#!/usr/bin/env python

from typing import List
from typing import Optional

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
		if len(nums) == 0:
			return None
		elif len(nums) == 1:
			return TreeNode(nums[0])
		else:
			val = max(nums)
			idx = nums.index(val)
			
			node = TreeNode(val, self.constructMaximumBinaryTree(nums[:idx]),
				self.constructMaximumBinaryTree(nums[idx + 1:]))

			return node
	
	def printNodes(self, node: TreeNode) -> None:
		if node == None:
			return

		print(node.val)
		self.printNodes(node.left)
		self.printNodes(node.right)

if __name__ == '__main__':
	nums = [3, 2, 1, 6, 0, 5]

	sol = Solution()
	node = sol.constructMaximumBinaryTree(nums)
	sol.printNodes(node)
