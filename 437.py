#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):

	def dfs(self, node, arr, sum, runningsum):
		if node != None:
			runningsum += node.val
			sumarr = arr + [node.val]

			cnt = 0
			totalsum = runningsum
			if totalsum == sum:
				cnt += 1
			
			for val in sumarr[:-1]:
				totalsum -= val
				if totalsum == sum:
					cnt += 1

			rcnt = self.dfs(node.left, arr + [node.val], sum, runningsum)
			lcnt = self.dfs(node.right, arr + [node.val], sum, runningsum)
			
			return cnt + rcnt + lcnt
		else:
			return 0
		
	def pathSum(self, root, sum):
		return self.dfs(root, [], sum, 0)

if __name__ == '__main__':
#	root = TreeNode(10)
#	root.left = TreeNode(5)
#
#	root.left.right = TreeNode(2)
#	root.left.right.right = TreeNode(1)
#
#	root.right = TreeNode(-3)
#	root.right.right = TreeNode(11)
#
#	root.left.left = TreeNode(3)
#
#	root.left.left.left = TreeNode(3)
#	root.left.left.right = TreeNode(-2)

	root = TreeNode(0)
	root.left = TreeNode(1)
	root.right = TreeNode(1)

	sol = Solution()
	print(sol.pathSum(root, 1))
