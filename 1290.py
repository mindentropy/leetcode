#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
class Solution(object):
	def getDecimalValue(self, head: ListNode)->int:
		num = 0
		while head:
			num <<= 1

			num |= head.val
			head = head.next

		return num

if __name__ == '__main__':

	head = ListNode(0)
	head.next = ListNode(0)

	sol = Solution()

	print(sol.getDecimalValue(head))
