#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isMirror(self, t1, t2):
		if t1 == None and t2 == None:
			return True

		if t1 == None or t2 == None:
			return False

		return t1.val == t2.val and self.isMirror(t1.right, t2.left) \
				and self.isMirror(t1.left, t2.right)
				
		
	def isSymmetric(self, root):
		"""
			:type root: TreeNode
			:rtype: bool
		"""
		return self.isMirror(root, root)
		

def construct_treenode():
	tn = TreeNode(1)
	tn.left = TreeNode(2)
	tn.right = TreeNode(2)
	
	tn.left.left = TreeNode(3)
	tn.left.right = TreeNode(4)
	tn.right.left = TreeNode(4)
	tn.right.right = TreeNode(3)

	return tn

if __name__ == '__main__':
	sol = Solution()
	print('Is symmetric : %s' % sol.isSymmetric(construct_treenode()))
