

#  A simple program to create a thing that 
#  is almost (but not quite) entirely unlike a Git repo. 

#  If Git were a drink, and a Nutri-Matic Drink 
#  Synthesizer attempted to make it, it would probably 
#  create something like this....   

#  Teagit - "Almost (but not quite) entirely unlike Git". 

#  Author:  mooseman 
#  This code is released to the public domain. 
#  "Share and enjoy"...... ;)  


import hashlib, os 

#  A class to create the repo-thingy (as the Captain would say...)   
class repo():
   	  
   # Initialise the "repo"
   # The list stores the data after the add.  	  
   # The dict stores the data when a commit is done. 
   def init(self, name):  
     self.tempdata = []       
     self.data = {} 
     self.name = name 
     print "Repo " + '"' + self.name + '"' + " is initialised" 	  
	  
   
   # Add data to the repo. 
   # Note - For now, this does not actually store any data - only 
   # the hexdigest string.  
   #  Add some data.   
   def add(self, pth):  
     f=open(pth,'rb').read()
     self.sh=hashlib.sha1(f).hexdigest() 	  
     self.dirname = self.sh[0:2]  
     self.tempdata.append(self.sh) 
     print "dirname is " + self.dirname 
     print "sha1hash is " + self.sh  
     print "Data added is " + str(self.tempdata) 
     return self.sh, self.dirname 
   
	   	  		 	  
   # Commit the data that has been added. 
   # Give a label to the "commit". 		  
   def commit(self, mylabel):	
      self.label = mylabel 
      for elem in self.tempdata: 
	     self.data[self.dirname] = elem   
   
	  
   #  Print the contents of the "repo"  
   def display(self):
	   for k,v in self.data:
		   print k, v
		   
		   	 	  
#  Test this cr^H^H code.... ;)  
myclass = repo() 

myclass.init('my repo') 

myclass.add('README')

myclass.commit("First commit") 

myclass.display() 


