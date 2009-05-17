

#  A simple program to create a thing that 
#  is almost (but not quite) entirely unlike a Git repo. 

#  If Git were a drink, and a Nutri-Matic Drink 
#  Synthesizer attempted to make it, it would probably 
#  create something like this....   

#  Teagit - "Almost (but not quite) entirely unlike Git". 

#  Author:  mooseman 
#  This code is released to the public domain. 
#  "Share and enjoy"...... ;)  


#  A class to create the repo-thingy (as the Captain would say...)   
class repo():
   # Name of the "repo"   	
   def setname(self, name):	   
      self.name = name 
	  
   # Initialise the "repo" 	  
   def init():
      data = {} 	  
	  
   # Get the SHA1 hash of the data. Pth is the path 
   # to the data.  	  
   def sha1hash(pth): 
	  f=open(pth,'rb').read()
	  sh=hashlib.sha1(f).hexdigest()
	  print sh 
	  return sh 	  
	  
   # Create the "dirname" from the first two characters of the 
   # hash hexdigest.  
   def dirname(sh): 	  
	  dirname = sh[0:2] 
	  print "dirname is " + dirname 
	  return dirname 
		  
   # Add data to the repo. Give a label to the "commit". 		  
   # Note - For now, this does not actually store any data - only 
   # the hexdigest string.  
   def commit(pth, label):	
      data[dirname] = sh  
	  
   #  Print the contents of the "repo"  
   def display(self):
	   for k,v in data:
		   print k, v
		   
		   	 	  
#  Test this cr^H^H code.... ;)  
myclass = repo() 

myclass.setname('test repo') 

myclass.sha1hash('README') 




  	  
