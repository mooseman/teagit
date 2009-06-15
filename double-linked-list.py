

#  double-linked-list.py 

#  This code is released to the public domain 


class Node:
   def __init__(self):
     self.prev = self.next = None

class LinkedList(Node):
   def __init__(self):  
     self.head = self.tail = None  
	 	 	 
   def append(self, node):
     if self.tail:
       self.tail.next = node
       node.prev = self.tail
     else:
       self.head = self.tail = node
	   
   def display(self): 
     print self 
	  	   
	   

a = LinkedList() 

a.__init__() 

a.append(1)

a.append(2) 

a.append(5) 

a.append(7) 



	   
