
#  dirwalk.py 
#  Try out the directory-walking functionality in Python. 
#  Acknowledgement - The first part of this code (to the end of the 
#  first for-loop) comes from the Python docs for os.walk() here - 
#  http://docs.python.org/library/os.html 

import os
from os.path import join, getsize

for root, dirs, files in os.walk('/home/andy/teagit'):
    print root, "consumes",
    print sum(int(getsize(join(root, name))) for name in files),             
    print "bytes in", len(files), "non-directory files"
    if '.git' in dirs:
        dirs.remove('.git')  # don't visit .git directories
     
#  Print a list of filenames and their sizes.         
for root, dirs, files in os.walk('/home/andy/teagit'):    
    for name in files: 
       print root, name, getsize(join(root, name)), " bytes"        
    if '.git' in dirs:
        dirs.remove('.git')  # don't visit .git directories    






