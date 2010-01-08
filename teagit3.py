

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

#  3 - Look at implementing a "staging area" to store "adds" before they  
#  are committed. 


import string, hashlib, zlib, gzip, os.path   

#  A file class 
#  Note on the "mode" - to get the mode of a file or directory, 
#  do the following - 
#  numeric_mode = os.stat('file_or_dir_name')[0]  
#  This creates a tuple with the stat details. The "mode" is the first 
#  element of the tuple.  We need to convert it to octal, as follows -
#  mymode = oct(numeric_mode & 0777)

#  A blob class.  
class blob(object): 
   def init(self):       
      self.blobdict = self.treedict = self.repodict = {} 
      self.prev = self.blobname = None 
   
   # Note - we may need to change this so that we can add TREES as well 
   # as blobs. Think about how to add trees.                 
   def add(self, mydata): 
      self.name = mydata 
      if os.path.isfile(mydata): 
         self.file = open(mydata, 'rb').read() 
         self.type = 'blob' 
      elif os.path.isdir(mydata):    
         self.type = 'tree' 
      self.size = str(int(os.path.getsize(mydata)))  
      self.mode = '10' + oct(os.stat(mydata)[0] & 0777)       
      # Header - different to Git    
      self.header = self.type + "*42*" + self.size + "moose" + "\0"          
      
      #  Calculate the SHA1 hexdigest.  
      self.stuff = self.header + self.file 
      self.sha1 = hashlib.sha1(self.stuff).hexdigest()    
      self.dirname = self.sha1[0:2]  
      self.blobname = self.sha1[2:41]  
            
      #  ( To do - calculate the SHA1s for a "tree" and a "commit". )      
      #  Save in our dict.  
      self.blobdict.update({ self.blobname: [self.dirname, self.prev, self.name, 
          self.size, self.mode ] })  
      # Now, the just-added data will be the "prev" instance for the next data to be added.  
      self.prev = self.blobname                    
          
      # Now create the TREE object for the blob. We do this when a 
      # commit is done. 
      # To do - Do the code to calculate a SHA1 for a tree and a 
      # commit. Also, fill the repodict dictionary with trees and blobs. 
      # Need to create a commit object. This will point to a tree, and 
      # will contain data like the author, a timestamp and a message. 
   def commit(self): 
      # First, we create a "tree" object. This is comprised of a header
      # and the data. We can do this by iterating through the 
      # directory, adding each "blob" (file) to the tree object. 
      
   
   
   
      for blob in self.blobdict.keys(): 
         self.treedict.update({ self.blobname: [self.mode, self.type, 
            self.name, self.size] })              
            
            
            
            
            
   def display(self): 
     print self.treedict 
     
     
#  Test the class 
a = blob() 
a.init() 
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
a.display()  



#  A tree class. This has the following attributes - 
#  mode, object-type (file or tree), file (or tree) name, 
#  objectID (which is the SHA1 hash of the object).  
class tree(blob): 
   def init(self): 
      self.prev = self.address = self.next = 0
      self.branch = "Main" 
      self.treedict = {} 

   # Add a blob or a tree.  
   def add(self, branch, data): 
      self.branch = branch 
      self.data = data        
      self.address = self.next 
      self.next += 1 
      self.treedict.update( {self.address: (self.branch, self.prev , self.next, self.data ) }) 
      self.prev = self.address  
            
   def display(self): 
      print self.treedict 
      
#  Run the code 
a = tree() 
a.init() 
a.add("Main", "foo bar baz") 
a.add("Main", (12, 43, 54, 68) ) 
a.add("Main", "Just a test")
a.display() 



class tree2(object): 
   def init(self): 
      self.data = {}   

   def add(self, mode, name, objectid): 
      self.mode = mode 
      self.name = name 
      self.object_type = name.object_type       
      self.objectid = objectid      
   
   def display(self): 
      print self.mode, self.object_type, self.name, self.objectid 
   
#  Create a few trees 
c = tree() 
d = tree() 
e = tree() 
   
         
#  A commit object. This object is made up of trees - it shows 
#  the state of a tree as at a given point in time. 
#  It also has metadata like the name of the committer, the commit 
#  date and time, and commint comments. 
#  The key is the SHA1 of the commit (which points to a tree). 
#  Then there are the SHA1s of the trees and blobs.   
class commit(object): 
   def __init__(self): 
      self.data = {} 
      self.prev = self.curr = None 
      self.object_type = "commit" 
      
   def add(self,tree): 
      self.data.update({ tree.objectid:  tree.name} ) 
      #  Update the prev and curr variables. 
      
      
   def display(self): 
      print self.data             
            
            
     
#  A Git tag class.  
class tag(object): 
   def init(self): 
      self.data = {} 
      
   def add(self, commit, desc): 
      self.tagID = commit.objectid 
      self.desc = desc 
      self.type = "tag" 
            
           
   
#  A "teagit object" class. This can be one of the following  
#  types - blob, tree, commit, tag. 
class teagitobject(object):
   def init(self): 
      self.data = {} 
      
   def add(self, obj): 
      self.object_id = obj.object_id 
      self.name = obj.name 
      self.obj_type = obj.type 
      self.data.update({ self.objectid: [self.name, self.obj_type] } ) 
      
                     
#  A repository object. This is a container for everything 
#  above. 
class repo(object): 
   def init(self): 
      self.data = {} 

   def add(self, path, repo, objects, refs, heads, HEAD): 
      self.path = path 
      self.repo = self.path + repo 
      self.objects = objects 
      self.refs = refs 
      self.heads = heads 
      self.HEAD = HEAD 

   # A method to display the contents of a given commit 
   def show_commit(self, commitID): 
      print self.data[commitID]   
                  
   def display(self): 
      print self.repo, self.objects, self.heads 
      
      
      
            
