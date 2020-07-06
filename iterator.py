class iterator:
 
 def __init__(self,name):
  self.name = name
  self.index = len(name)
 
 def __iter__(self):
  return(self)
  
 def __next__(self):
  if(self.index!=0):
   self.index-=1
   return(self.name[self.index])
  else:
   raise StopIteration   
  
n = iterator("shefali")
for i in n:
 print(i)
"""k = iter(n.name)
for x in range(len(n.name)):
 print(k.__next__(), end='')"""

