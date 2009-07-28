

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

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
#  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
#  ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

 
#  TO DO - 
#  1 - Get the most basic functionality working. 
#  That is - get a file's name, mode (permissions) and 
#  its SHA1 hash.  Save these to disk (probably using pickle). 

#  2 - Start on computing diffs on files. Find out exactly 
#  what changes in a file from revision to revision. 
#  ( Note to self: Git apparently uses "libxdiff" to calculate diffs. 
#  find out more about that library. )  

#  3 - Look at implementing the Git index. It is the contents 
#  of this (not the working directory) that are added in a commit. 


import hashlib, zlib, gzip, os.path   

#  A file class 
#  Note on the "mode" - to get the mode of a file or directory, 
#  do the following - 
#  numeric_mode = os.stat('file_or_dir_name')[0]  
#  This creates a tuple with the stat details. The "mode" is the first 
#  element of the tuple.  We need to convert it to octal, as follows -
#  mymode = oct(numeric_mode & 0777)
#  This will give you '0644' for a file, and '0755' for a directory 
#  ( a "tree" in Git terms ) 
#  For a file (a 'blob'), Git adds '10' to the front of the mode to 
#  give you the string '100644' 
#  For a directory, Git simply gives it the mode '040000'.    

#  A useful command for testing - 
#  git hash-object filename   ( gives Gits SHA1 hash for a file )  

  
  
#  A class to get the Git SHA1 objectID of a file or tree. 
class sha(object): 
   def init(self): 
      self.data = {}  
      self.prev = self.blobname = None 
               
   def add(self, mydata): 
      self.name = mydata 
      self.file = open(mydata, 'rb').read() 
      self.size = str(int(os.path.getsize(mydata)))  
      self.mode = '10' + oct(os.stat(mydata)[0] & 0777) 
      if self.mode in ('100644' , '100755'): 
         self.type = 'blob' 
      else: 
         self.type = 'tree'       
      self.header = self.type + " " + self.size + "\0"          
      self.stuff = self.header + self.file 
      self.sha1 = hashlib.sha1(self.stuff).hexdigest()    
      self.dirname = self.sha1[0:2]  
      self.blobname = self.sha1[2:41]    
      # self.data.update({ self.blobname: [self.dirname, self.prev, self.name, self.size, self.mode ] })  
      
      # Now, the just-added data will be the "prev" instance for the next data to be added.  
      self.prev = self.blobname     
      
      # Now, create the tree object to hold the blob   
      # Test data - This should give the following hash - 
      # dbb95599c651ffa577f79647c8a66c7225b30b6d
      # "blob" "42"\0"100644 small_file.txt"\0b1e9ced39154adb38cfa26c652e017566ae2c7d9
      
      # A VERY HANDY COMMAND TO GET THE CONTENTS OF A GIVEN HASH 
      # $ echo SHA1hash | git cat-file --batch 
      # For example - 
      # $ echo 05b217bb859794d08bb9e4f7f04cbda4b207fbe9 | git cat-file --batch

      
      self.tree_header = "tree" + " " + self.size + "\0" 
      self.tree_data = self.mode + " " + self.name + "\0" + self.sha1  
      self.tree_stuff = self.tree_header + self.tree_data 
      self.tree_sha1 = hashlib.sha1(self.tree_stuff).hexdigest()   
      self.data.update({ self.blobname: [self.tree_sha1 ] })  
                           
   def display(self): 
     print self.data  
     
          
#  Test the class 
a = sha() 
a.init() 
a.add('Vitai-Lampada.txt') 
a.add('small_file.txt') 
a.display()  



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
      
      
      
            
