#!/usr/bin/env python


class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next
		
class Solution(object):
	def swapNodes(self, head: ListNode, k: int) -> ListNode:
		runner = head
		node = head

		cnt = k
		while (cnt) > 1:
			runner = runner.next
			node = node.next
			cnt -= 1

		follower = head
		runner = runner.next

		while runner != None:
			follower = follower.next
			runner = runner.next
		
		node.val, follower.val = follower.val, node.val

		return head
		

if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(3)
	node.next.next.next = ListNode(4)
	node.next.next.next.next = ListNode(5)


	sol = Solution()

	head = sol.swapNodes(node, 2)

	while head != None:
		print(head.val)
		head = head.next
