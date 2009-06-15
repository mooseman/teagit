

#  double-linked-list.py 

#  This code is released to the public domain 


class Node:
   def __init__(self):
     self.prev = self.next = None


''' TO DO:  Add a list to keep track of added keys so that 
we can track their parent (if any) and the HEAD. ''' 

class LinkedList():
   def init(self):     
     ''' Create the dictionary to hold the keys and data. ''' 
     ''' Mydict is the main dictionary.  Keydict is the 
     dictionary that we use to hold the realtionships between 
     keys. In other words, parent/child relationships and which 
     key is the HEAD.  ''' 
     self.mydict = {} 
     self.keydict = {}   
     self.parent = self.head = 0  
	 
   ''' Add data to the list '''    
   def append(self,node_num, branch_name, data):
     ''' Add the data '''  
     ''' TO DO - add test here to test if this is the FIRST commit 
     to the dictionary. Also assign the HEAD and PARENT node 	 	 
	 flags.  ''' 
	   
     self.key = (node_num, branch_name) 
     self.mydict[self.key] = data 
     
     
     
     '''self.keydict.update(zip(self.key, None)) '''
     '''self.head = self.keydict[self.key]  '''
     ''' self.parent = ? ''' 
	 	 	
			 		  
   ''' Remove data from the list ''' 	   
   def remove(self, node_num):  
     ''' Will complete this later. ''' 
     pass 
	 
   ''' Display the current data. ''' 	 
   def display(self, key):
     if key == "all": 
	    print self.mydict  
     elif self.mydict.has_key(key):
		'''print self.mydict[key] '''   
		print key, self.mydict[key] 
     else: 
	    print "Sorry: key not found..."  		
	 
#  Run the code 
a = LinkedList()  
a.init()  

a.append(1, "main", "foobarbaz")  

a.append(2, "main", "Just a little test....")

a.append(3, "main", "And another test....")   
	 	    	   
a.append(4, "main", "Very cool!!!")

a.append(5, "main", "Linked lists are GREAT!")

a.display("all") 

a.display((3, "main")) 



	   
	   

	   
