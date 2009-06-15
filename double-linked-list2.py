

#  double-linked-list.py 

#  This code is released to the public domain 


class Node:
   def __init__(self):
     self.prev = self.next = None

class LinkedList(Node):
   def __init__(self):
     self.head = self.tail = None  
	 ''' Create the dictionary to hold the keys and data. ''' 
	 self.treedict = {} 
	 ''' a) Create a list for the dictionary keys. We use a tuple for 
	        the keys to allow for branches and multiple parent nodes. 
	     b) Populate the list. 
		 c) Convert the list to a tuple (so we can use it in the 
		    dictionary). ''' 
     self.dictlist = []
	 
   ''' Add data to the list ''' 	 	 
   def append(self, node_num, branch_name, data):
     if self.tail:
       self.tail.next = node_num
       node.prev = self.tail
     else:
       self.head = self.tail = node_num 
	   
   ''' Remove data from the list ''' 	   
   def remove(self, node_num):  
     pass ''' Will complete this later. ''' 
	 
   ''' Display the current data. ''' 	 
   def display(self): 
     print self.treedict  
	 
	 
#  Run the code 
a = Linked_List()  
a._init_()  

a.append(1, "main", "foobarbaz")  

a.append(2, "main", "Just a little test....")

a.append(3, "main", "And another test....")   
	 	    	   
a.append(4, "main", "Very cool!!!")

a.append(5, "main", "Linked lists are GREAT!")

	   
	   

	   
