#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def oddEvenList(self, head):
		oddnode = head
		oddhead = oddnode
		
		if head == None:
			return head

		if oddnode.next == None or oddnode.next.next == None:
			return oddnode

		evennode = oddnode.next
		evenhead = evennode

		while oddnode != None and oddnode.next != None and oddnode.next.next != None:
			tmp = oddnode
			oddnode = oddnode.next.next
			evennode.next = oddnode.next
			evennode = evennode.next
			tmp.next = oddnode
		
		if tmp.next != None:
			tmp.next.next = evenhead
		else:
			tmp.next = evenhead

		
	#	tmp = head
	#	while tmp != None:
	#		print(tmp.val)
	#		tmp = tmp.next

		return head

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(4)
	node.next.next.next.next = ListNode(5)
	node.next.next.next.next.next = ListNode(6)

	sol = Solution()
	sol.oddEvenList(node)
