#!/usr/bin/env python

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		prev = None
		curr = head
		nxt = None

		if head == None:
			return None

		if head.next == None:
			return head

		while(curr):
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

		return prev

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(4)
	node.next.next.next.next = ListNode(5)

	sol = Solution()
	head = sol.reverseList(node)

	while head:
		print head.val
		head = head.next

