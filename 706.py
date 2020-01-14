#!/usr/bin/env python

## Standard hashmap. Will not be accepted because of the space complexity.
#class MyHashMap(object):
#	
#	def __init__(self):
#		self.map = [-1] * 1000000
#
#	def put(self, key, value):
#		self.map[key] = value
#
#	def get(self, key):
#		return self.map[key]
#
#	def remove(self, key):
#		self.map[key] = -1

class ListNode(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None

## Chained hashmap
class MyHashMap(object):
	def __init__(self):
		self.map = [None] * 1000

	def put(self, key, value):
		hashkey = key % 1000

		if self.map[hashkey] == None:
			self.map[hashkey] = ListNode(key, value)
		else:
			tmp = self.map[hashkey]

			prev = None
			while tmp != None:
				## If there is already value present overwrite
				if tmp.key == key:
					tmp.val = value
					return

				prev = tmp
				tmp = tmp.next

			prev.next = ListNode(key, value)
	
	def get(self, key):

		hashkey = key % 1000
		if self.map[hashkey] == None:
			return -1
		else:
			tmp = self.map[hashkey]

			while tmp != None:
				if tmp.key == key:
					return tmp.val

				tmp = tmp.next

			return -1

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

if __name__ == '__main__':
	hashMap = MyHashMap()

	hashMap.put(1, 1)
	hashMap.put(2, 2)
	print hashMap.get(1)
	print hashMap.get(3)
	hashMap.put(2, 1)
	print hashMap.get(2)
	hashMap.remove(2)
	print hashMap.get(2)
