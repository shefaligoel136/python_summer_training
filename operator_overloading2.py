class a:
 def __init__(self,m1):
  self.m1 = m1
 
 def __gt__(obj1,obj2):
  if obj1.m1>obj2.m1:
   return obj1.m1
  else:
   return obj2.m1
   

s1 = a(13)
s2 = a(55)
print(s1>s2)
