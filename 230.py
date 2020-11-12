#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def __init__(self):
		self.k = 0
		self.val = 0
		self.found = False

	def binsearch(self, node):
		if node != None and not self.found:
			self.binsearch(node.left)

			if self.k == 0:
				#print(node.val)
				if self.found == False:
					self.val = node.val
					self.found = True
				return
			else:
				self.k -= 1

			self.binsearch(node.right)

	def kthSmallest(self, root, k):
		self.k = k - 1
		self.binsearch(root)

		return self.val

#	def kthSmallest(self, root , k):
#		return self.binsearch(root, k - 1)

if __name__ == '__main__':
	node = TreeNode(3)
	node.left = TreeNode(1)
	node.left.right = TreeNode(2)
	node.right = TreeNode(4)

	sol = Solution()
	print(sol.kthSmallest(node, 1))
	
