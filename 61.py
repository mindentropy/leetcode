#!/usr/bin/env python

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def rotateRight(self, head:ListNode, k: int) -> ListNode:
		if head == None:
			return head

		cnt = 0
		node = head
		while node != None:
			node = node.next
			cnt += 1

		k = k % cnt

		runner = head
		if k == 0:
			return head

		while k > 0:
			runner = runner.next
			k -= 1

		if runner == head:
			return head

		follower = head
		tmp  = None
		tmp_follow = None
		while runner != None:
			tmp = runner
			tmp_follow = follower
			runner = runner.next
			follower = follower.next
		
		tmp.next = head
		head = follower
		tmp_follow.next = None

		return head

if __name__ == '__main__':
	sol = Solution()

	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(4)
	node.next.next.next.next = ListNode(5)

#	node = ListNode(1)
#	node.next = ListNode(2)
#	node.next.next = ListNode(2)

	head = sol.rotateRight(node, 2)

	while head != None:
		print(head.val)
		head = head.next
