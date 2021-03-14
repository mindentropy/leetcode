#!/usr/bin/env python

class Node(object):
	def __init__(self, val, prev = None, next = None, child = None):
		self.val = val
		self.prev = prev
		self.next = next
		self.child = child

class Solution(object):

	def serialize(self, head):
		
		node = head
		prev = None

		while node != None:
			if node.child != None:
				tmp = self.serialize(node.child)
				tmp.next = node.next

				if node.next != None:
					node.next.prev = tmp

				node.next = node.child
				node.child.prev = node
				node.child = None

				prev = tmp
				node = tmp.next

			else:
				prev = node
				node = node.next

		return prev
	
	def flatten(self, head):
		self.serialize(head)
		return head

if __name__ == '__main__':
#	node = Node(1)
#	node.next = Node(2, node)
#	node.next.next = Node(3, node.next)
#	node.next.next.next = Node(4, node.next.next)
#	node.next.next.next.next = Node(5, node.next.next.next)
#	node.next.next.next.next.next = Node(6, node.next.next.next.next)
#
#	node.next.next.child = Node(7)
#	node.next.next.child.next = Node(8, node.next.next.child)
#	node.next.next.child.next.next = Node(9, node.next.next.child.next)
#	node.next.next.child.next.next.next = Node(10, node.next.next.child.next.next)
#	node.next.next.child.next.child = Node(11)
#	node.next.next.child.next.child.next = Node(12, node.next.next.child.next.child)

#	tmp = node.next.next.child.next.child
#	while tmp != None:
#		print(tmp.val)
#		tmp = tmp.next

	node = Node(1)
	node.child = Node(2)
	node.child.child = Node(3)

	sol = Solution()
	node = sol.flatten(node)

	prev = None
	while node != None:
		print(node.val)
		prev = node
		node = node.next
	
	print("------------")
	tmp = prev 
	while tmp!= None:
		print(tmp.val)
		tmp = tmp.prev

