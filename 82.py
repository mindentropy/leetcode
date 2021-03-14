#!/usr/bin/env python

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		node = head

		follower = None
		while node != None:
			runner = node.next
			while runner != None and runner.val == node.val:
				runner = runner.next
			
			if node.next != runner:
				if follower == None:
					head = node = runner
				else:
					node = follower.next = runner
			else:
				follower = node
				node = node.next

		return head
					

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(3)
	node.next.next.next.next = ListNode(4)
	node.next.next.next.next.next = ListNode(4)
	node.next.next.next.next.next.next = ListNode(5)
	
	sol = Solution()
	head = sol.deleteDuplicates(node)

	while head != None:
		print(head.val)
		head = head.next
