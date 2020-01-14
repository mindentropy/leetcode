#!/usr/bin/env python

class ListNode(object):
	def __init__(self, key):
		self.key = key
		self.next = None

class MyHashSet(object):
	
	def __init__(self):
		self.map = [None] * 1000
	
	def add(self, key):
		hashkey = key % 1000

		if self.map[hashkey] == None:
			self.map[hashkey] = ListNode(key)
		else:
			tmp = self.map[hashkey]

			prev = None
			while tmp != None:

				## If there is already key present return
				if tmp.key == key:
					return

				prev = tmp
				tmp = tmp.next

			prev.next = ListNode(key)

	def remove(self, key):
		hashkey = key % 1000

		if self.map[hashkey] != None:
			tmp = self.map[hashkey]
			
			prev = None
			while tmp != None:
				if tmp.key == key:
					if tmp == self.map[hashkey]:
						self.map[hashkey] = tmp.next
						tmp.next = None
						del tmp
						return
					else:
						prev.next = tmp.next
						tmp.next = None
						del(tmp)
						return

				prev = tmp
				tmp = tmp.next
	
	def contains(self, key):
		hashkey = key % 1000
		if self.map[hashkey] == None:
			return False
		else:
			tmp = self.map[hashkey]

			while tmp != None:
				if tmp.key == key:
					return True

				tmp = tmp.next

			return False

if __name__ == '__main__':

	hashset = MyHashSet()
	hashset.add(1)
	hashset.add(2)
	print hashset.contains(1)
	print hashset.contains(3)

	hashset.add(2)
	print hashset.contains(2)
	hashset.remove(2)
	print hashset.contains(2)
