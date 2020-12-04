#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def __init__(self):
		self.maxcnt = 1
	
	def inorder(self, node, prevnode, cnt):
		if node != None:
			if prevnode != None and node.val == prevnode.val:
				return 1
			else:
				return 0

			cnt + self.inorder(node.left, prevnode, cnt)

		else:
			return 0

#		if node != None:
#			if prevnode != None and node.val == prevnode.val:
#				cnt += 1
#			else:
#				if self.maxcnt < cnt:
#					self.maxcnt = cnt
#
#				cnt = 1
#
#			self.inorder(node.left, node, cnt)
#			self.inorder(node.right, node, cnt)
	
	def longestUnivaluePath(self, root):
		self.inorder(root, None, 0)

		return self.maxcnt

if __name__ == '__main__':
	root = TreeNode(5)
	root.right = TreeNode(5)
#	root.left = TreeNode(4)
#	root.left.left = TreeNode(1)
#	root.left.right = TreeNode(1)
#
#	root.right = TreeNode(5)
#	root.right.right = TreeNode(5)

	sol = Solution()
	print(sol.longestUnivaluePath(root))
