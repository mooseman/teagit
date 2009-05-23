

#  double-linked-list.py 

#  This code is released to the public domain 


class Node:
   def __init__(self):
     self.prev = self.next = None

class LinkedList:
   def __init__(self):
     self.head = self.tail = None
   def append(self, node):
     if self.tail:
       self.tail.next = node
       node.prev = self.tail
     else:
       self.head = self.tail = node
	   

	   
