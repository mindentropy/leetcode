#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def numComponents(self, head, G):
		node = head
		cnt = 0

		while node != None:
			if node.val in G and (node.next == None or node.next.val not in G):
				cnt += 1
			
			node = node.next

		return cnt

if __name__ == '__main__':
	node = ListNode(0)
	node.next = ListNode(1)
	node.next.next = ListNode(2)
	node.next.next.next = ListNode(3)
	
	G = [0, 1, 3]

	sol = Solution()
	print(sol.numComponents(node, G))
