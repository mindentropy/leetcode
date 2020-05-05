#!/usr/bin/env python

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:


	def isPalindrome(self, head:ListNode) -> bool:

		slow = fast = head

		while(fast != None and fast.next != None):
			fast = fast.next.next
			slow = slow.next

		
		#Reverse the linked list
		prev = None
		curr = head
		nxt = None

		while curr != slow:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

		curr = prev
		if fast:
			slow = slow.next

		while curr != None and slow != None:

			if curr.val != slow.val:
				return False

			curr = curr.next
			slow = slow.next


		if curr == None and slow == None:
			return True

if __name__ == '__main__':

	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(1)

	sol = Solution()
	print(sol.isPalindrome(head))
