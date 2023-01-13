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
		head = head.next
		prev = None
		prevpair = None

		while odd != None and odd.next != None:
			tmp1 = odd.next.next
			tmp2 = odd.next
			odd.next = tmp1
			tmp2.next = odd

			if prevpair != None:
				prev = prevpair
				prev.next = tmp2

			prevpair = odd
			odd = tmp1
			
		return head

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
#	node.next.next.next = ListNode(4)

	sol = Solution()
	head = sol.swapPairs(node)

	while head != None:
		print(head.val)
		head = head.next
