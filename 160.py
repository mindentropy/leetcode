#!/usr/bin/env python

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA: ListNode,
					headB: ListNode) -> ListNode:

		a_len = 0
		b_len = 0
	
		tmpa = headA
		tmpb = headB

		while tmpa != None or tmpb != None:
			if tmpa != None:
				a_len += 1
				tmpa = tmpa.next

			if tmpb != None:
				b_len += 1
				tmpb = tmpb.next

		skip_dist = 0

		if a_len > b_len:
			dist = a_len - b_len

			while(dist != 0):
				headA = headA.next
				dist -= 1
		elif b_len > a_len:
			dist = b_len - a_len
			
			while(dist != 0):
				headB = headB.next
				dist -= 1
		
		while headA != headB and headA != None and headB != None:
			headA = headA.next
			headB = headB.next

		if headA == None or headB == None:
			return None
		
		if headA == headB:
			return headA
			

#		while headA != None:
#			tmp = headB
#			while tmp != None:
#				if tmp == headA:
#					return tmp
#
#				tmp = tmp.next
#
#			headA = headA.next
#
#		return None

if __name__ == '__main__':
	sol = Solution()
	
	headA = ListNode(4)
	headA.next = ListNode(1)

	headA.next.next = ListNode(8)
	headA.next.next.next = ListNode(4)
	headA.next.next.next.next = ListNode(5)

	headB = ListNode(5)
	headB.next = ListNode(0)
	headB.next.next = ListNode(1)

	headB.next.next.next = headA.next.next


	print(sol.getIntersectionNode(headA, headB).val)

