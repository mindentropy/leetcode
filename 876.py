#!/usr/bin/env python

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def middleNode(self, head):
		
		slow = head
		fast = head

		while fast != None and fast.next != None:
			slow = slow.next
			fast = fast.next.next

		return slow

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(4)
	node.next.next.next.next = ListNode(5)
	node.next.next.next.next.next = ListNode(6)

	sol = Solution()
	print sol.middleNode(node).val
