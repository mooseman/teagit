

#  Levenshtein.py 
# Playing around with SHA1 and the Levenshtein function
# This code is released to the public domain. 
# Acknowledgement - The Levenshtein code here was written by 
# Magnus Lie Hetland. Very many thanks to Magnus for doing that code!

import string, hashlib 

# dicts to store the line-numbers and lines  
linedict1 = linedict2 = {} 
# dicts to store the line-numbers and hashes 
hashdict1 = hashdict2 = {}

# A dict to store the diffs between files
diffsdict = {} 


# Open a file 
f1 = open("file1.txt", "r").readlines() 
for i, line in enumerate(f1): 
   linedict1.update({i: line})   
   m = hashlib.sha1(line).hexdigest()
   hashdict1.update({i: m}) 
   
for k, v in hashdict1.items(): 
   print k, v 
   
for k, v in linedict1.items(): 
   print k, v 

# Open a second file 
f2 = open("file2.txt", "r").readlines() 
for j, line in enumerate(f2): 
   linedict2.update({j: line})   
   n = hashlib.sha1(line).hexdigest()
   hashdict2.update({j: n}) 
   
for k, v in hashdict2.items(): 
   print k, v 
   
for k, v in linedict2.items(): 
   print k, v 


# The Levenshtein distance between two strings  
def levenshtein(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n] 
    
        
# Find the differences between the two files 
# Note - need to look at how to find if a line has been moved (but not 
# changed). This could be done by appending the line number (and a 
# separator) to the hash. If the result only differs by line number, 
# then the line has been moved.  
for x in list(zip(hashdict1.items(), hashdict2.items() )): 
   if x[0][1] != x[1][1]: 
      print x[0][1]
   else: 
      pass 
         
         
   
   
'''for c, d in zip((linedict1.values(), linedict2.values() )):  
    if a != b: 
       e = levenshtein(linedict1[c], linedict2[d])
       diffsdict.update({a: e})     
    else: 
        pass '''
        
'''for k, v in diffsdict.items(): 
   print k, v  '''
   
               
       
        
    
       
       
       
           
    
      
   
      


