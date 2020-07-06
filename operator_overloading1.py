class a:
 def __init__(self,m1,m2):
  self.m1 = m1
  self.m2 = m2
 
 def __add__(obj1,obj2):
  x = obj1.m1+obj2.m2
  y = obj1.m1+obj2.m2
  z = a(x,y)
  return z

s1 = a(3,4)
s2 = a(44,55)
s3 = s1+s2
print(s3.m1)  
print(s3.m2)  