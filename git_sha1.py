

#  git_sha1.py 

# A simple program to find the "Git ObjectID" of a file. 
  
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


import hashlib, zlib, gzip, os.path   


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

#  A very useful command for testing - 
#  git hash-object filename   ( gives Gits SHA1 objectID for a file )  

    
#  A class to get the Git SHA1 objectID of a file. 
class sha(object): 
   def init(self): 
      self.data = None       
               
   def add(self, mydata): 
      self.file = open(mydata, 'rb').read() 
      self.size = str(int(os.path.getsize(mydata)))  
      self.mode = '10' + oct(os.stat(mydata)[0] & 0777) 
      if self.mode == '100644': 
         self.type = 'blob' 
      else: 
         self.type = 'tree'       
      self.header = self.type + " " + self.size + "\0"          
      self.data = self.header + self.file 
      self.sha1 = hashlib.sha1(self.data).hexdigest()                   
      
   def display(self): 
     print self.sha1 
     
     
#  Test the class 
a = sha() 
a.init() 
a.add('Vitai-Lampada.txt') 
a.display()  

b = sha() 
b.init() 
b.add('small_file2.txt') 
b.display()

c = sha() 
c.init() 
c.add('small_file.txt') 
c.display()






      
            
