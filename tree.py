

#  A tree class 

class tree():   
   	  
   # Initialise the "repo"
   # The list stores the data after the add.  	  
   # The dict stores the data when a commit is done. 
   def init(self, name):  
     self.dirnamelist = []    
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
     self.gitfilename = self.sh[3:41] 
     self.dirnamelist.append(self.dirname)   	 
     self.tempdata.append(self.gitfilename) 
        	   	  		 	 
   # Commit the data that has been added. 
   # Give a label to the "commit". 		  
   def commit(self, mylabel):	
      self.label = mylabel 	  
      self.data.update(zip(self.dirnamelist, self.tempdata) )   
      	  
   #  Print the contents of the "repo"  
   def display(self):
	   print self.data 
	   
		   		   	 	  
#  Test this cr^H^H code.... ;)  
myclass = tree() 

myclass.init('my repo') 

myclass.add('README') 

myclass.add('Vitai-Lampada.txt') 

myclass.add('Mary-had-a-great-big-moose.txt') 

myclass.commit("First commit") 

myclass.display() 

    

	   	     
	 
