#!/usr/bin/env python

class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	
	def bfs(self, root):
		lst = [root]
		numarr = []

		numflip = 0
		while len(lst) != 0:
			arr = []
			lvlnode = []

			while len(lst) != 0:
				node = lst.pop(0)
				
				if numflip & 1 == 0:
					arr.extend([node.val])
				else:
					arr.insert(0,node.val)

				if node.left != None:
					lvlnode.append(node.left)

				if node.right != None:
					lvlnode.append(node.right)

			numarr.append(arr)
			lst.extend(lvlnode)

			numflip += 1

		return numarr
	
	def zigzagLevelOrder(self, root):
		if root == None:
			return []

		return self.bfs(root)

if __name__ == '__main__':

#	root = TreeNode(3)
#	root.left = TreeNode(9)
#	root.right = TreeNode(20)
#	root.right.left = TreeNode(15)
#	root.right.right = TreeNode(7)

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.right.right = TreeNode(5)

	sol = Solution()
	print(sol.zigzagLevelOrder(root))
