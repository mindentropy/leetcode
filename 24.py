#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def swapPairs(self, head):
		if head == None or head.next == None:
			return head

		odd = head
		even = head.next
		head = even

		oddprev = None
		evenprev = odd
		
		oddnext = None
		evennext = None
		
		while odd != None:
			
			if even.next == None:
				evennext = None
			else:
				evennext = even.next.next

			oddnext = odd.next.next

			odd.next = evennext
			even.next = odd

			even = evennext
			odd = oddnext

		return head
	#	while head != None:
	#		print(head.val)
	#		head = head.next

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)

	sol = Solution()
	sol.swapPairs(node)
