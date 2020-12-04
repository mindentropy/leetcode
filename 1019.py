#!/usr/bin/env python

class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val 
		self.next = next

class Solution(object):
	def nextLargerNodes(self, head):
		next_max_arr = []
		stk = []
		node = head

		if node.next == None:
			return [0]

		stk.append((node.val, 0))
		next_max_arr.append(0)
		node = node.next

		idx2 = 1
		while node != None:
			if node.val > stk[-1][0]:
				idx = len(next_max_arr) - 1
				while stk != []:
					if node.val > stk[-1][0]:
						next_max_arr[stk[-1][1]] = node.val
						stk.pop()
						idx -= 1
					else:
						break

			stk.append((node.val, idx2))
			
			next_max_arr.append(0)
			node = node.next
			idx2 += 1

		return next_max_arr

if __name__ == '__main__':

#	head = ListNode(2)
#	head.next = ListNode(1)
#	head.next.next = ListNode(5)

	#[2, 7, 4, 3, 5]
#	head = ListNode(2)
#	head.next = ListNode(7)
#	head.next.next = ListNode(4)
#	head.next.next.next = ListNode(3)
#	head.next.next.next.next = ListNode(5)

#	head = ListNode(1)
#	head.next = ListNode(7)
#	head.next.next = ListNode(5)
#	head.next.next.next = ListNode(1)
#	head.next.next.next.next = ListNode(9)
#	head.next.next.next.next.next = ListNode(2)
#	head.next.next.next.next.next.next = ListNode(5)
#	head.next.next.next.next.next.next.next = ListNode(1)

	head = ListNode(9)
	head.next = ListNode(7)
	head.next.next = ListNode(6)
	head.next.next.next = ListNode(7)
	head.next.next.next.next = ListNode(6)
	head.next.next.next.next.next = ListNode(9)

	node = head
	while node != None:
		print(node.val, end=' ')
		node = node.next

	print("")

	sol = Solution()
	print(sol.nextLargerNodes(head))
