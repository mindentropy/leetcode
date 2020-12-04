#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	
	def dfs(self, node, arr, totalsum, sum):
		if node != None:
			totalsum += node.val
			if node.left == None and node.right == None:
				if totalsum == sum:
					#print(arr + [node.val])
					return [arr + [node.val]]
				else:
					return []

			leftarr = self.dfs(node.left, arr + [node.val], totalsum, sum)
			rightarr = self.dfs(node.right, arr + [node.val], totalsum, sum)
			
			totalarr = []
			if leftarr != []:
				totalarr.extend(leftarr)

			if rightarr != []:
				totalarr.extend(rightarr)

			return totalarr

		else:
			return []
		
	def pathSum(self, root, sum):
		return self.dfs(root, [], 0, sum)
		
if __name__ == '__main__':
#	root = TreeNode(5)
#	root.left = TreeNode(4)
#	root.left.left = TreeNode(11)
#	root.left.left.left = TreeNode(7)
#	root.left.left.right = TreeNode(2)
#
#	root.right = TreeNode(8)
#	root.right.left = TreeNode(13)
#	root.right.right = TreeNode(4)
#	root.right.right.left = TreeNode(5)
#	root.right.right.right = TreeNode(1)

	root = TreeNode(1)

	sol = Solution()
	print(sol.pathSum(root, 1))
