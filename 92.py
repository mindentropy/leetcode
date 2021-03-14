#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):

	def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
		if left == right:
			return head

		cnt = 0
		node = head
		prev_left = None

		while cnt+1 != left:
			cnt += 1
			prev_left = node
			node = node.next

		leftnode = node

		prev = prev_left
		curr = leftnode
		nxt = None

		while cnt + 1 <= right:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
			cnt += 1

		if prev_left != None:
			prev_left.next = prev
		else:
			head = prev

		leftnode.next = nxt
		
		return head

#	def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#		if left == right:
#			return head
#
#		cnt = 0
#		node = head
#		prev_left = None
#
#		while cnt+1 != left:
#			cnt += 1
#			prev_left = node
#			node = node.next
#
#		leftnode = node
#
#		while cnt+1 != right:
#			cnt += 1
#			node = node.next
#
#		rightnode = node
#		next_right = rightnode.next
#
#		prev = prev_left
#		curr = leftnode
#		nxt = None
#
#		while curr != next_right:
#			nxt = curr.next
#			curr.next = prev
#			prev = curr
#			curr = nxt
#
#		if prev_left != None:
#			prev_left.next = rightnode
#		else:
#			head = rightnode
#
#		leftnode.next = next_right
#		
#		return head

#	def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#		node = head
#		stk = []
#
#		if left == right:
#			return head
#
#		cnt = 0
#
#		while node != None and (cnt + 1) != left:
#			node = node.next
#			cnt += 1
#
#		leftnode = node
#
#		while node != None and (cnt + 1) != right:
#			stk += [node.val]
#			node = node.next
#			cnt += 1
#
#		stk += [node.val]
#		rightnode = node
#
#		while len(stk):
#			leftnode.val = stk.pop()
#			leftnode = leftnode.next
#
#		return head
if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(4)
	node.next.next.next.next = ListNode(5)

	sol = Solution()
	head = sol.reverseBetween(node, 1, 5)

	while head != None:
		print(head.val)
		head = head.next
