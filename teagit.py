

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
   # Name of the "repo"   	
   def setname(self, name):	   
      self.name = name 
	  
   # Initialise the "repo" 	  
   def init(self):
	  self.data = {} 
	  print "Repo is initialised" 	  
	  
   # Get the SHA1 hash of the data. Pth is the path 
   # to the data. 
   # Suppress the call to "self".  
   # @staticmethod   	  
   def sha1hash(self, pth): 
	  f=open(pth,'rb').read()
	  self.sh=hashlib.sha1(f).hexdigest() 	  
	  self.dirname = self.sh[0:2]  
	  print "dirname is " + self.dirname 
	  print "sha1hash is " + self.sh  
	  return self.sh, self.dirname  	  
	  
		  
   # Add data to the repo. Give a label to the "commit". 		  
   # Note - For now, this does not actually store any data - only 
   # the hexdigest string.  

   def commit(self, mylabel):	
	   self.data[self.dirname] = self.sh  
	   self.label = mylabel 
	  
   #  Print the contents of the "repo"  
   def display(self):
	   for k,v in self.data:
		   print k, v
		   
		   	 	  
#  Test this cr^H^H code.... ;)  
myclass = repo() 

myclass.init() 

myclass.setname('test repo') 

myclass.sha1hash('README')

print myclass.name 

myclass.commit("First commit") 

myclass.display() 



   

  




  	  
