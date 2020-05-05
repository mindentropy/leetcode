#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def tree2str(self, t):
		if t == None:
			return ''
		elif t.left == None and t.right == None:
			return str(t.val) + ''
		elif t.right == None:
			return str(t.val) + '(' + self.tree2str(t.left) + ')'
		elif t.left == None:
			return str(t.val) + '()(' + self.tree2str(t.right) + ')'
		else:
			return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
	
if __name__ == '__main__':
	sol = Solution()
	t = TreeNode(1)
	t.left = TreeNode(2)
	t.left.left = TreeNode(4)
	
	t.right = TreeNode(3)

	print sol.tree2str(t)
