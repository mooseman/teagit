

#  double-linked-list.py 

#  This code is released to the public domain 


class Node:
   def __init__(self):
     self.prev = self.next = None


class LinkedList():
   def init(self):     
     ''' Create the dictionary to hold the keys and data. ''' 
     self.mydict = {} 
	 
   ''' Add data to the list '''    
   def append(self,node_num, branch_name, data):
     ''' Add the data '''  
     ''' TO DO - add test here to test if this is the FIRST commit 
     to the dictionary. Also assign the HEAD and PARENT node 	 	 
	 flags.  ''' 
	   
     self.key = (node_num, branch_name) 
     self.mydict[self.key] = data 
     self.head = self.mydict[self.key]  
	 	 	 		  
   ''' Remove data from the list ''' 	   
   def remove(self, node_num):  
     ''' Will complete this later. ''' 
     pass 
	 
   ''' Display the current data. ''' 	 
   def display(self): 
     print self.mydict  
	 
	 
#  Run the code 
a = LinkedList()  
a.init()  

a.append(1, "main", "foobarbaz")  

a.append(2, "main", "Just a little test....")

a.append(3, "main", "And another test....")   
	 	    	   
a.append(4, "main", "Very cool!!!")

a.append(5, "main", "Linked lists are GREAT!")

a.display() 

	   
	   

	   
