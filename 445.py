#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		num1 = 0
		num2 = 0

		while l1 != None and l2 != None:
			num1 *= 10
			num1 += l1.val

			num2 *= 10
			num2 += l2.val

			l1 = l1.next
			l2 = l2.next

		while l1 != None:
			num1 *= 10
			num1 += l1.val

			l1 = l1.next

		while l2 != None:
			num2 *= 10
			num2 += l2.val

			l2 = l2.next

		total = num1 + num2
		
		if total == 0:
			return ListNode(0)

		prev = None
		while total != 0:
			node = ListNode(total % 10)
			node.next = prev
			prev = node

			total = int(total / 10)

		return prev

if __name__ == '__main__':
	numlst1 = ListNode(7)
	numlst1.next = ListNode(2)
	numlst1.next.next = ListNode(4)
	numlst1.next.next.next = ListNode(3)

	numlst2 = ListNode(5)
	numlst2.next = ListNode(6)
	numlst2.next.next = ListNode(4)

	sol = Solution()
	node = sol.addTwoNumbers(numlst1, numlst2)

	while node != None:
		print(node.val,end='')
		node = node.next
