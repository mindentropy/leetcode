#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def removeElements(self, head: ListNode, val: int) -> ListNode:

		prev = None 
		node = head
			
		while node != None:
			if node.val == val:
				if prev == None:
					head = node.next
					node = node.next
				else:
					prev.next = node.next
					node = node.next
			else:
				prev = node
				node = node.next

		return head

if __name__ == '__main__':

	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(6)
	node.next.next.next = ListNode(3)
	node.next.next.next.next = ListNode(4)
	node.next.next.next.next.next = ListNode(5)
	node.next.next.next.next.next.next = ListNode(6)

	sol = Solution()
	head = sol.removeElements(node, 6)

	while head != None:
		print(head.val)
		head = head.next

