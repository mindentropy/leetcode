#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def dfs(self, root, runningsum, totalsum):
		if root != None:
			runningsum += root.val
			
			if root.left == None and root.right == None:
				if runningsum == totalsum:
					return True
				elif runningsum > totalsum:
					return False
			
			return self.dfs(root.left, runningsum, totalsum) or\
				self.dfs(root.right, runningsum, totalsum)
		else:
			return False
		
	def hasPathSum(self, root, sum):
		return self.dfs(root, 0, sum)

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
#	root.right.right.right = TreeNode(1)

	root = TreeNode(-2)
	root.right = TreeNode(-3)

	sol = Solution()
	print(sol.hasPathSum(root, -5))
