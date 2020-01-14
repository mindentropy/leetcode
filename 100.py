#!/usr/bin/env python

class Solution(object):
	
	def isSameTree(self, p, q):
		if(p == None and q == None):
			return True
		elif((p != None and q == None) or (p == None and q != None)):
			return False
#		else:
#			return p.val == q.val and self.isSameTree(p.right, q.right) and \
#							self.isSameTree(p.left, q.left)
		elif p.val != q.val:
			return False
		else:
			r1 = self.isSameTree(p.right, q.right) 
			r2 = self.isSameTree(p.left, q.left)
			return (r1 and r2)

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

if __name__ == '__main__':
	p = TreeNode(1)
	p.left = TreeNode(2)
	p.right = TreeNode(3)

	q = TreeNode(1)
	q.left = TreeNode(2)
	q.right = TreeNode(3)

	sol = Solution()
	print(sol.isSameTree(p, q))
