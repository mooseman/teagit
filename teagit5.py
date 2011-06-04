

#  teagit.py 

# A simple program to create a thing that
# is almost (but not quite) entirely unlike a Git repo.
 
# If Git were a drink, and a Nutri-Matic Drink
# Synthesizer attempted to make it, it would probably
# create something like this....
  
# Author: mooseman

# Acknowledgements: A very big "thank you" to the developers of 
# Git - the DVCS that rules the universe. First written by Linus 
# Torvalds and now maintained by Junio Hamano - you guys rock!  
# Also a big "thank you" to Scott Chacon for his work on the 
# "Git Community Book" - an *outstanding* resource for learning 
# all about Git!    

# This code is released to the public domain.
# "Share and enjoy"...... ;) 

 
#  TO DO - 
#  1 - Get the most basic functionality working. 
#  That is - get a file's name, mode (permissions) and 
#  its SHA1 hash.  Save these to disk (probably using pickle). 

#  2 - Focus on using SHA1 hashes - they're the key to tracking the 
#  state of a repo and its contents over time.  

import sys, string, hashlib, zlib, gzip, os.path   
from os.path import join, getsize

#  A repo class 
#  A commit has a SHA1 ID, and points to a tree. 
#  Trees are made up of blobs and other trees. 
#  Blobs are standalone objects. 
#  A commit has metadata like the name of the committer, the commit 
#  date and time, and commit comments. 
#  The key is the SHA1 of the commit (which points to a tree). 
#  Then there are the SHA1s of the trees and blobs.   
class repo(object): 
   def __init__(self):       
      self.staging = self.trees = self.commits = {}      
      #self.stuff = []       
      # Note - we may need to change this so that we can add TREES as well 
      # as blobs. Think about how to add trees.                 
   def add(self, mydata): 
      self.name = mydata 
      if os.path.isfile(mydata): 
         self.file = open(mydata, 'rb').read() 
         self.size = int(os.path.getsize(mydata))
         self.type = 'blob' 
      elif os.path.isdir(mydata):    
         self.size = 0             
         self.file = [] 
         #  Print a list of filenames and their sizes.         
         for root, dirs, files in os.walk(mydata):                 
            self.size += sum(int(getsize(join(root, name))) for name in files)                       
            for name in files:                 
                self.file.append([root, name, getsize(join(root, name))]) 
                #self.size += int(os.path.getsize(join(root, name)))
            if '.git' in dirs:
                dirs.remove('.git')  # don't visit .git directories        
         self.type = 'tree'       
      self.mode = '10' + oct(os.stat(mydata)[0] & 0777)       
      # Header - different to Git    
      self.header = self.type + "*42*" + str(self.size) + "moose" + "\0"          
      
      #  Calculate the SHA1 hexdigest.  
      if self.type == 'blob': 
         self.stuff = self.header + self.file 
      elif self.type == 'tree':    
         self.stuff = self.header + str(self.file)          
      self.sha1 = hashlib.sha1(self.stuff).hexdigest()    
      self.dirname = self.sha1[0:2]  
      self.blobname = self.sha1[2:41]  
            
      #  ( To do - calculate the SHA1s for a "tree" and a "commit". )      
      #  Save in our dict.  
      self.staging.update({ self.blobname: [self.dirname, self.name, 
          self.size, self.mode ] })  
               
   # A remove method, to remove things from the "staging area".  
   def remove(self, stuff): 
      pass 
                           
   def commit(self): 
      # First, we create a "tree" object. This is comprised of a header
      # and the data. We can do this by iterating through the 
      # directory, adding each "blob" (file) to the tree object.                
      for obj in self.staging.keys(): 
         self.trees.update({ self.blobname: [self.mode, self.type, 
            self.name, self.size] })              
         self.commits.update({ self.blobname: [self.mode, self.type, 
            self.name, self.size] })    
                     
   def display(self, obj=None): 
      if obj == None: 
         print self.commits             
      else:          
         for k, v in self.commits.items(): 
            if k.startswith(obj): 
               print k, v
               sys.exit() 
            else: 
               print "Object not found"    
               sys.exit()   
                
                                             
#  Test the class 
a = repo() 
a.add('file1.txt') 
a.add('file2.txt') 
a.commit() 
a.add('Vitai-Lampada.txt') 
a.commit()
a.add('test') 
a.commit()
# Need to fix. This is giving the same SHA1 code as adding the "test" 
# directory. This means that it is not added to the dict because the dict
# must have unique keys. 
a.add('.')
a.commit()
#a.display()  
# Print a specified object 
a.display('2ac') 

      
                     
