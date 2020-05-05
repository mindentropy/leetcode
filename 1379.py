#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.clone_tgt = None

#	def getTgtCopy(self, original, cloned, target):
#		if original != None and self.clone_tgt == None:
#			self.getTargetCopy(original.left, cloned.left, target)
#			if original == target:
#				self.clone_tgt = cloned
#			self.getTargetCopy(original.right, cloned.right, target)
#
#	def getTargetCopy(self, original, cloned, target):
#		self.getTgtCopy(original, cloned, target)
#		return self.clone_tgt

	def getTargetCopy(self, original, cloned, target):
		if original == None:
			return None
		elif original == target:
			return cloned
		else:
			res = self.getTargetCopy(original.left, cloned.left, target)
			if res != None:
				return res
			else:
				return self.getTargetCopy(original.right, cloned.right, target)

if __name__ == '__main__':
	orig = TreeNode(7)
	orig.left = TreeNode(4)
	orig.right = TreeNode(3)
	orig.right.left = TreeNode(6)
	orig.right.right = TreeNode(19)

	
	cloned = TreeNode(7)
	cloned.left = TreeNode(4)
	cloned.right = TreeNode(3)
	cloned.right.left = TreeNode(6)
	cloned.right.right = TreeNode(19)

	sol = Solution()
	print sol.getTargetCopy(orig, cloned, orig.right).val
