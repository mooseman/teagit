

#  new_teagit.py 

#  A new version of teagit which tries to make more use 
#  of classes. This is aimed at coming a bit closer to 
#  the way that Git fits together. 
 
#  TO DO - 
#  1 - Get the most basic functionality working. 
#  That is - get a file's name, mode (permissions) and 
#  its SHA1 hash.  Save these to disk (probably using pickle). 

#  2 - Start on computing diffs on files. Find out exactly 
#  what changes in a file from revision to revision. 

#  3 - Look at implementing the Git index. It is the contents 
#  of this (not the working directory) that are added in a commit. 


import hashlib 

#  A file class 
class file(object): 
   def __init__(self):  
      self.data = {}  
      
   def add(self, fname): 
      self.file = open(fname,'rb').read() 
      self.sh=hashlib.sha1(file).hexdigest() 	  
      self.dirname = self.sh[0:2]  
      self.gitfilename = self.sh[3:41] 
      self.data.update({ self.sh:  [self.file, self.dirname, self.gitfilename] })   
            
   def display(self):
      print self.data   
      
      
#  Create a file or two 
a = file()
b = file() 
       
      
            
#  A blob class. A blob contains the contents 
#  of a file - it is a binary "blob" of data. 
class blob(object):  
   def init(self): 
      self.data = {} 
      
   def add(self, file): 
      self.fname = file.fname 
      self.objectid = file.objectid  
      self.type = "blob" 
             
      
        
#  A tree class. This has the following attributes - 
#  mode, object-type (file or tree), file (or tree) name, 
#  objectID (which is the SHA1 hash of the object).  
class tree(object): 
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
a = tree() 

a.init() 

a.add("Main", "foo bar baz") 

a.add("Main", (12, 43, 54, 68) ) 



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
#  The key is the objectid.  
class commit(object): 
   def __init__(self): 
      self.data = {} 
      self.prev = self.curr = self.next = None 
      self.object_type = "commit" 
      
   def add(self,tree): 
      self.data.update({ tree.objectid:  tree.name} ) 
      #  Update the prev, curr and next variables. 
            
     
#  A Git tag class.  
class tag(object): 
   def init(self): 
      self.data = {} 
      
   def add(self, commit, desc): 
      self.tagID = commit.objectid 
      self.desc = desc 
      self.type = "tag" 
            
           
   
#  A Git object class. A git object can be one of the following  
#  types - blob, tree, commit, tag. 
class gitobject(object):
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
      
      
      
            
