#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Solution(object):
	def rangeSumBST(self, root, L, R):
			if root == None:
				return 0
			elif root.val >= L and root.val <= R:
				return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) 
			elif root.val > R:
				return self.rangeSumBST(root.left, L, R)
			elif root.val < L:
				return self.rangeSumBST(root.right, L, R)

if __name__ == '__main__':

	t = TreeNode(10)
	t.left= TreeNode(5)
	t.left.left = TreeNode(3)
	t.left.right = TreeNode(7)
	t.right = TreeNode(15)
	t.right.right = TreeNode(18)
	
	sol = Solution()
	print(sol.rangeSumBST(t, 7, 15))

	
	#sol.rangeSumBST()
