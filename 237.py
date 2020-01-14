#!/usr/bin/env python

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, node):
		prev = None
		while node.next:
			prev = node
			node.val = node.next.val
			node = node.next

		prev.next = None


if __name__ == '__main__':
	node = ListNode(4)
	node.next = ListNode(5)
	node.next.next = ListNode(1)
	node.next.next.next = ListNode(9)

	sol = Solution()
	sol.deleteNode(node.next.next)

	while node:
		print node.val
		node = node.next
