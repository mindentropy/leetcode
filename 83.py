#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
class Solution(object):
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		
		if head == None:
			return head

		prev = head
		curr = head.next

		while curr:
			if curr.val == prev.val:
				prev.next = curr.next
			else:
				prev = curr

			curr = curr.next

		return head

if __name__ == '__main__':

	headnode = ListNode(1)
	headnode.next = ListNode(1)
	headnode.next.next = ListNode(2)
	headnode.next.next.next = ListNode(3)
	headnode.next.next.next.next = ListNode(3)

	sol = Solution()
	head = sol.deleteDuplicates(headnode)

	while(head):
		print(head.val)
		head = head.next
