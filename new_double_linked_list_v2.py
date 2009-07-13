

#  new_double_linked_list.py 
#  An attempt at a double-linked list class. 
#  Author: Andy Elvey 
#  This code is released to the public domain. 
#  "Share and enjoy......"  :)  


class dll(object): 
   def init(self): 
      self.prev = self.address = self.next = 0
      self.branch = "Main" 
      self.nodedict = {} 

   def add(self, branch, data): 
      self.branch = branch 
      self.data = data        
      self.address = self.next 
      self.next += 1 
      self.nodedict.update( {self.address: (self.branch, self.prev , self.next, self.data ) }) 
      self.prev = self.address  
            
   def display(self): 
      print self.nodedict 
      
#  Run the code 
a = dll() 

a.init() 

a.add("Main", "foo bar baz") 

a.add("Main", (12, 43, 54, 68) ) 

a.add("Main", "Mary had a little lamb") 

a.add("Test", "Share and enjoy....") 

a.add("Test", "Ayyyyyye... LUX-ury!") 

a.display() 

            
      
